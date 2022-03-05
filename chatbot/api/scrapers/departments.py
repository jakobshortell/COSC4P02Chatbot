import mechanicalsoup
import sqlite3
from bs4 import BeautifulSoup, Comment

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
					social TEXT,
					description TEXT,
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
                'email': self.get_email(department),
                'social': self.get_social(department),
                'description': self.get_description(department)
            }

            output[index] = entry

        # Store info in the database
        self.store_departments(output)

        return output

    def get_name(self, department):
        '''Extracts the name from a department.'''
        try:
            n = department.find('h2', attrs={
                'class': 'name'
            }).text
            if ', ' in n:
                name = n.split(', ')
                return name[1] + " " + name[0]
            else:
                return n
        except:
            return "N/A"

    def get_link(self, department):
        '''Extracts the link from a department.'''
        try:
            return department.find('div', attrs={
                'class': 'link'
            }).find('a')['href']
        except:
            return "N/A"

    def get_social(self, department):
        '''Extracts the social from a department.'''
        try:
            return department.find('div', attrs={
                'class': 'social'
            }).find('a')['href']
        except:
            return "N/A"

    def get_description(self, department):
        '''Extracts the social from a department.'''
        try:
            soup = BeautifulSoup(str(department), 'lxml')
            comments = str(soup.findAll(text=lambda text: isinstance(text, Comment)))
            i = comments.find('<p>') + 3
            comments = comments[i : : ]
            i = comments.find('</p>')
            comments = comments[ :i: ]
            return comments
        except:
            return "N/A"

    def get_extension(self, department):
        '''Extracts the phone extension from a department.'''
        try:
            phone = department.find('div', attrs={
                'class': 'phone'
            }).find('small').text
            if "x" in phone:
                return "(905) 688-5550 " + phone
            else:
                return phone
        except:
            return "(905) 688-5550"

    def get_email(self, department):
        '''Extracts the email from a department.'''
        try:
            return department.find('div', attrs={
                'class': 'email'
            }).find('a').text.lower()
        except:
            return "N/A"

    def store_departments(self, departments):
        '''Adds the clubs to the database.'''
        with self.db_conn as conn:
            for index in departments:
                conn.execute(
                    '''
					INSERT OR REPLACE INTO departments
					VALUES (?, ?, ?, ?, ?, ?)
					''',
                    (
                        departments[index]['name'],
                        departments[index]['link'],
                        departments[index]['extension'],
                        departments[index]['email'],
                        departments[index]['social'],
                        departments[index]['description']
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
                'email': row['email'],
                'social': row['social'],
                'description': row['description']
            }

        return output
