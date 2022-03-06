import sqlite3
from requests_html import HTMLSession

class CoursesScraper:

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
				CREATE TABLE IF NOT EXISTS courses (
					program_code TEXT, 
                    course_code TEXT,
					title TEXT, 
					duration TEXT,
					day TEXT,
                    time TEXT,
                    type TEXT,
                    instructor TEXT,
                    section INTEGER,
                    location TEXT,
					PRIMARY KEY (course_code, duration, type)
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
        output = self.get_program_courses()

        # If program codes is empty, fetch hasn't been run
        if not output:
            self.fetch()
            return self.get()

        return output

    def fetch_program_codes(self):
        '''Returns a list of all the program codes at Brock University.'''
        response = self.session.get('https://brocku.ca/guides-and-timetables/timetables/?session=fw&type=ug&level=all')
        response.html.render()

        # Get list of programs
        programs_list = response.html.find('span.code')
        program_codes = [program.text for program in programs_list]

        response.close()
        return program_codes

    def fetch_program_courses(self, code):
        '''Returns a dictionary containing all program courses at Brock University.'''
        response = self.session.get(f'https://brocku.ca/guides-and-timetables/timetables/?session=FW&type=UG&level=All&program={code}')
        response.html.render(sleep=3, timeout=15)

        # Find all courses
        course_rows = response.html.find('tr.course-row')
        courses = {}

        # Loop through the rows
        for index, row in enumerate(course_rows):
            courses[index] = {
                'program_code': code,
                'course_code': self.fetch_course_code(row),
                'title': self.fetch_course_title(row),
                'duration': self.fetch_course_duration(row),
                'day': self.fetch_course_day(row),
                'time': self.fetch_course_time(row),
                'type': self.fetch_course_type(row),
                'instructor': self.fetch_course_instructor(row),
                'section': self.fetch_course_section(row),
                'location': self.fetch_course_location(row)
            }

        # Store courses in the database
        self.store_courses(courses)

        response.close()
        return courses

    def fetch_course_code(self, row):
        '''Extracts the course code from the course row.'''
        return row.find('td.course-code', first=True).text

    def fetch_course_title(self, row):
        '''Extracts the course title from the course row.'''
        return row.find('td.title', first=True).find('a', first=True).text

    def fetch_course_duration(self, row):
        '''Extracts the course duration from the course row.'''
        return row.find('td.duration', first=True).text

    def fetch_course_day(self, row):
        '''Extracts the course day from the course row.'''
        try:
            # Return the index of the active day
            day_list = ""
            days = row.find('td.days', first=True).find('tbody', first=True).find('td')
            for index, day in enumerate(days):
                if 'active' in day.attrs['class']:
                    day_list = day_list + " " + self.days[index]
            return day_list

        except:
            return "N/A"

    def fetch_course_time(self, row):
        '''Extracts the course time from the course row.'''
        try:
            return row.find('td.time', first=True).text
        except:
            return "N/A"

    def fetch_course_type(self, row):
        '''Extracts the course type from the course row.'''
        return row.find('td.type', first=True).text

    def fetch_course_instructor(self, row):
        '''Extracts the course instructor from the course row.'''
        return row.attrs['data-instructor']

    def fetch_course_section(self, row):
        '''Extracts the course section from the course row.'''
        return row.attrs['data-course_section']

    def fetch_course_location(self, row):
        '''Extracts the course location from the course row.'''
        return row.attrs['data-location']

    def store_courses(self, courses):
        '''Adds courses to the database.'''
        with self.db_conn as conn:
            for index in courses:
                conn.execute(
					'''
					INSERT OR REPLACE INTO courses 
					VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
					''', 
					(
                        courses[index]['program_code'],
						courses[index]['course_code'],
                        courses[index]['title'],
                        courses[index]['duration'],
                        courses[index]['day'],
                        courses[index]['time'],
                        courses[index]['type'],
                        courses[index]['instructor'],
                        courses[index]['section'],
                        courses[index]['location']
					)
				)
                conn.commit()

    def get_program_codes(self):
        '''Gets all the program codes from the database and returns them as a list.'''
        with self.db_conn as conn:
            rows = conn.execute(
                '''
                SELECT DISTINCT program_code
                FROM courses
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
                FROM courses
                '''
            ).fetchall()

        # Add courses to dictionary
        for index, row in enumerate(rows):
            output[index] = {
                'program_code': row['program_code'],
                'course_code': row['course_code'],
                'title': row['title'],
                'duration': row['duration'],
                'day': row['day'],
                'time': row['time'],
                'type': row['type'],
                'instructor': row['instructor'],
                'section': row['section'],
                'location': row['location']
            }

        return output