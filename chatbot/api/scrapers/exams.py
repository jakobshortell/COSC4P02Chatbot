import sqlite3
from requests_html import HTMLSession


class ExamScraper:

    def __init__(self):
        self.session = HTMLSession()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row
        self.days = {
            0: 'Sunday',
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday'
        }

        # Create database tables
        with self.db_conn as conn:
            conn.execute(
                '''
				CREATE TABLE IF NOT EXISTS exams (
					program_code TEXT, 
                    course_code TEXT,
					duration TEXT,
					section TEXT,
					day TEXT,
					start TEXT,
                    end TEXT,
                    location TEXT,
					PRIMARY KEY (course_code, duration, section)
				)
				'''
            )
            conn.commit()

    def fetch(self):
        '''Fetches course offerings from Brock and stores it in the database.'''
        program_codes = self.fetch_program_codes()
        output = {}

        for code in program_codes:
            output[code] = self.fetch_program_courses(code)

        return output

    def get(self):
        '''Gets courses from the chatbot database.'''
        output = {}
        # Get all courses for each program code
        output = self.get_program_courses()

        return output

    def fetch_program_codes(self):
        '''Returns a list of all the program codes having exams at Brock University.'''
        response = self.session.get('https://brocku.ca/guides-and-timetables/timetables/?session=fw&type=ex&level=all')
        response.html.render()

        # Get list of programs
        programs_list = response.html.find('span.code')
        program_codes = [program.text for program in programs_list]
        response.close()
        return program_codes

    def fetch_program_courses(self, code):
        '''Returns a dictionary containing all program courses at Brock University.'''
        response = self.session.get(
            f'https://brocku.ca/guides-and-timetables/timetables/?session=fw&type=ex&level=all&program={code}')
        response.html.render(sleep=3, timeout=15)

        # Find all courses
        course_rows = response.html.find('tr.exam-row')
        courses = {}

        # Loop through the rows
        for index, row in enumerate(course_rows):
            courses[index] = {
                'program_code': code,
                'course_code': self.fetch_course_code(row),
                'duration': self.fetch_course_duration(row),
                'section': self.fetch_course_section(row),
                'day': self.fetch_course_day(row),
                'start': self.fetch_course_start(row),
                'end': self.fetch_course_end(row),
                'location': self.fetch_course_location(row)
            }

        # Store courses in the database
        self.store_courses(courses)

        response.close()
        return courses

    def fetch_course_code(self, row):
        '''Extracts the course code from the course row.'''
        return row.find('td.course-code', first=True).text

    def fetch_course_duration(self, row):
        '''Extracts the course duration from the course row.'''
        return row.find('td.duration', first=True).text

    def fetch_course_day(self, row):
        '''Extracts the course day from the course row.'''
        return row.find('td.day', first=True).text

    def fetch_course_start(self, row):
        '''Extracts the course time from the course row.'''
        return row.find('td.start', first=True).text

    def fetch_course_end(self, row):
        '''Extracts the course type from the course row.'''
        return row.find('td.end', first=True).text

    def fetch_course_section(self, row):
        '''Extracts the course section from the course row.'''
        return row.find('td.section', first=True).text

    def fetch_course_location(self, row):
        '''Extracts the course location from the course row.'''
        return row.find('td.location', first=True).text

    def store_courses(self, exams):
        '''Adds courses to the database.'''
        with self.db_conn as conn:
            for index in exams:
                conn.execute(
                    '''
					INSERT OR REPLACE INTO exams 
					VALUES (?, ?, ?, ?, ?, ?, ?, ?)
					''',
                    (
                        exams[index]['program_code'],
                        exams[index]['course_code'],
                        exams[index]['duration'],
                        exams[index]['section'],
                        exams[index]['day'],
                        exams[index]['start'],
                        exams[index]['end'],
                        exams[index]['location']
                    )
                )
                conn.commit()

    def get_program_codes(self):
        '''Gets all the program codes from the database and returns them as a list.'''
        with self.db_conn as conn:
            rows = conn.execute(
                '''
                SELECT DISTINCT program_code
                FROM exams
                '''
            ).fetchall()

        # Extracts the program code from the row
        rows = [row['program_code'] for row in rows]

        return rows

    def get_program_courses(self):
        '''Gets all the courses from the database and returns them as a dictionary.'''
        output = {}

        # Pull all courses from the database
        with self.db_conn as conn:
            rows = conn.execute(
                '''
                SELECT *
                FROM exams
                '''
            ).fetchall()

        # Add courses to dictionary
        for index, row in enumerate(rows):
            output[index] = {
                'program_code': row['program_code'],
                'course_code': row['course_code'],
                'duration': row['duration'],
                'section': row['section'],
                'day': row['day'],
                'start': row['start'],
                'end': row['end'],
                'location': row['location']
            }

        return output