import re
import sqlite3

import mechanicalsoup


class CoursesDetailsScraper:

    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row

        # Create database tables
        with self.db_conn as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS details (
                    course_code TEXT,
                    course_name TEXT, 
                    alt_course_code TEXT,
                    course_description TEXT, 
                    hours TEXT,
                    restrictions TEXT,
                    prerequisite TEXT,
                    corequisite TEXT,
                    notes TEXT,
                    replace_grade TEXT,
                    PRIMARY KEY (course_code, course_name)
                )
                '''
            )
            conn.commit()

    def fetch(self):
        """Fetches course details from Brock and stores it in the database."""
        output = {}
        program_links = self.fetch_programs()
        # Visit all the program links that were found
        for link in program_links:
            output[link.text] = self.fetch_course_details(link)

        return output

    def get(self):
        '''Gets course details from the chatbot database.'''
        output = self.get_program_courses()

        # If program codes is empty, fetch hasn't been run
        if not output:
            self.fetch()
            return self.get()

        return output

    def get_program_courses(self):
        '''Gets all the course details from the database and returns them as a dictionary.'''
        output = {}

        # Pull all course details from the database
        with self.db_conn as conn:
            rows = conn.execute(
                '''
                SELECT *
                FROM details
                '''
            ).fetchall()

        # Add courses to dictionary
        for index, row in enumerate(rows):
            output[index] = {
                'course_code': row['course_code'],
                'course_name': row['course_name'],
                'alt_course_code': row['alt_course_code'],
                'course_description': row['course_description'],
                'hours': row['hours'],
                'restrictions': row['restrictions'],
                'prerequisite': row['prerequisite'],
                'corequisite': row['corequisite'],
                'notes': row['notes'],
                'replace_grade': row['replace_grade']

            }

        return output

    def fetch_course_details(self, page_link):
        '''Extracts course details from a given page in the brock calendar'''
        output = {}
        self.browser.follow_link(page_link)
        # Get the text version of the site
        course_details = self.browser.page.get_text()
        # Turn the raw text into something that can be used
        course_details = self.find_courses(course_details)
        for index, course in enumerate(course_details):
            # Since we don't know what data this course actually has, so we need to find it
            # We know that indexes 0 and 1 always will hold course code and name, so they don't need to be evaluated

            code_and_description = self.get_alt_course_code_and_desc(
                course[2:4])
            details = self.fetch_details(course[3:])
            entry = {
                'course_code': course[0],
                'course_name': course[1],
                'alt_course_code': code_and_description[0],
                'course_description': code_and_description[1],
                'hours': details[0],
                'restrictions': details[1],
                'prerequisite': details[2],
                'corequisite': details[3],
                'notes': details[4],
                'replace_grade': details[5]

            }
            output[index] = entry

        # Store info in the database
        self.store_course_details(output)

        return output

    def find_courses(self, course_details):
        """Gets rid of all unnecessary parts of the website, keeping only the course and their details"""
        only_details = []
        # The pattern of how course codes appear in the file
        search_pattern = '^[A-Z][A-Z][A-Z][A-Z] [0-9][A-Z][0-9][0-9]$'
        # remove # and * because they are not necessary for this and make pattern matching more difficult
        course_details = course_details.replace('#', '')
        course_details = course_details.replace('*', '')
        # Separate each line
        split_lines = course_details.split("\n")
        # Remove whitespace from front and back of each entry
        split_lines = [item.strip() for item in split_lines]
        # Find where the course codes actually start
        split_lines = self.find_details_start(split_lines)
        for i in range(len(split_lines)):
            # find if the current line contains a course code as the start of it
            search_results = re.search(search_pattern, split_lines[i])
            # if this line has a course code and there is text directly below that code add it to the list of courses
            if search_results is not None and split_lines[i + 1] != '':
                arr = []
                # a course has been found, now copy all of its associated info to an array
                while split_lines[i] != '':
                    arr.append(split_lines[i])
                    i += 1
                only_details.append(arr)
        return only_details

    def get_alt_course_code_and_desc(self, course):
        """Determines if there is another code for this course"""
        # If there is an alternate code it will be at [0] with the description at index 1, if there is not an alternate
        # code, the course description will be at index 0 and the info at index 1 will need to be analyzed later
        other_offer = re.search('also offered as ', course[0])
        if other_offer is not None:
            return course[0][other_offer.end(): -1], course[1]
        else:
            # there is no cross listing for this course
            return '', course[0]

    def store_course_details(self, output):
        with self.db_conn as conn:
            for index in output:
                conn.execute(
                    '''
                    INSERT OR REPLACE INTO details 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (
                        output[index]['course_code'],
                        output[index]['course_name'],
                        output[index]['alt_course_code'],
                        output[index]['course_description'],
                        output[index]['hours'],
                        output[index]['restrictions'],
                        output[index]['prerequisite'],
                        output[index]['corequisite'],
                        output[index]['notes'],
                        output[index]['replace_grade']
                    )
                )
                conn.commit()

    def fetch_details(self, course):
        """Get course details that don't always appear in the same index"""
        details = [''] * 6
        hours_search_terms = '^Lecture|^Seminar|^Lab|^Tutorial|^Online|^Theory|^Workshop|^Laboratories|^Field Trip,'
        for index in course:
            hours = re.search(hours_search_terms, index, re.IGNORECASE)
            restriction = re.search('Restriction: ', index)
            prerequisite = re.search('Prerequisite\(s\): ', index)
            corequisite = re.search('Corequisite\(s\): ', index)
            notes = re.search('Note: ', index)
            replace_grade = re.search(
                'Completion of this course will replace previous', index)
            if hours is not None:
                details[0] = index[:-1]
            elif restriction is not None:
                details[1] = index[restriction.end(): -1]
            elif prerequisite is not None:
                details[2] = index[prerequisite.end(): -1]
            elif corequisite is not None:
                details[3] = index[corequisite.end(): -1]
            elif notes is not None:
                details[4] = index[notes.end(): -1]
            elif replace_grade is not None:
                details[5] = index

        return details

    def fetch_programs(self):
        """Finds the list of links for program that will need to be scraped"""
        start_index = 0
        self.browser.open('https://brocku.ca/webcal/undergrad/')
        all_page_links = self.browser.links()
        for index, link in enumerate(all_page_links):
            # The list of programs is in between "Life at Brock" and "Undeclared Arts and Undeclared Science"
            # Find the index of each and return the list of program URLs to visit
            if re.search('Life at Brock', link.text) is not None:
                start_index = index + 1
            if re.search('Undeclared Arts and Undeclared Science', link.text) is not None:
                return all_page_links[start_index:index]

    def find_details_start(self, course_details):
        found_count = 0
        for index, line in enumerate(course_details):
            if re.search('Prerequisites and Restrictions', line):
                found_count += 1
            if found_count == 2:
                return course_details[index:]
        return course_details
