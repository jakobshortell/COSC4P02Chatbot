import mechanicalsoup
import sqlite3


class DepartmentScraper:

    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row

        # Create database tables
        with self.db_conn as conn:
            conn.execute(
                '''
				CREATE TABLE IF NOT EXISTS departments (
					name TEXT, 
					link TEXT, 
					extension TEXT,
					email TEXT,
					PRIMARY KEY (name)
				)
				'''
            )
            conn.commit()

    def fetch(self):
        '''Fetches department data from Brock and stores it in the database.'''
        self.browser.open('https://brocku.ca/directory/a-z/')
        departments_list = self.browser.page.find_all('div', attrs={'class': 'item'})
        return self.read_departments(departments_list)

    def get(self):
        '''Gets departments from the chatbot database.'''

        # Pull club data from database
        departments = self.get_departments()

        # If database had no info, fetch new info
        if not departments:
            self.fetch()
            return self.get_departments()
            
        return departments

    def read_departments(self, departments_list):
        '''Extracts data from the list of departments.'''
        output = {}

        for index, department in enumerate(departments_list):
            # Pull department information
            entry = {
                'name': self.get_name(department),
                'link': self.get_link(department),
                'extension': self.get_extension(department),
                'email': self.get_email(department)
            }

            output[index] = entry

        # Store info in the database
        self.store_departments(output)

        return output

    def get_name(self, department):
        '''Extracts the name from a department.'''
        try:
            return department.find('h2', attrs={
                'class': 'name'
            }).text
        except:
            return None

    def get_link(self, department):
        '''Extracts the link from a department.'''
        try:
            return department.find('div', attrs={
                'class': 'link'
            }).find('a')['href']
        except:
            return None

    def get_extension(self, department):
        '''Extracts the phone extension from a department.'''
        try:
            return department.find('div', attrs={
                'class': 'phone'
            }).find('small').text
        except:
            return None

    def get_email(self, department):
        '''Extracts the email from a department.'''
        try:
            return department.find('div', attrs={
                'class': 'email'
            }).find('a').text.lower()
        except:
            return None

    def store_departments(self, departments):
        '''Adds the clubs to the database.'''
        with self.db_conn as conn:
            for index in departments:
                conn.execute(
                    '''
					INSERT OR REPLACE INTO departments
					VALUES (?, ?, ?, ?)
					''',
                    (
                        departments[index]['name'],
                        departments[index]['link'],
                        departments[index]['extension'],
                        departments[index]['email']
                    )
                )
                conn.commit()

    def get_departments(self):
        '''Gets all the departments from the database and returns them as a dictionary.'''
        output = {}

        # Pull all departments from database
        with self.db_conn as conn:
            rows = conn.execute(
                '''
				SELECT *
				FROM departments
				'''
            ).fetchall()

        # Add departments to dictionary
        for index, row in enumerate(rows):
            output[index] = {
                'name': row['name'],
                'link': row['link'],
                'extension': row['extension'],
                'email': row['email']
            }

        return output