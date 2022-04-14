import mechanicalsoup
import sqlite3


class ProgramScraper:

    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row

        # Create database tables
        with self.db_conn as conn:
            conn.execute(
                '''
				CREATE TABLE IF NOT EXISTS programs (
					name TEXT, 
					description TEXT,
					prerequisites TEXT,
					PRIMARY KEY (name)
				)
				'''
            )
            conn.commit()

    def fetch(self):
        '''Fetches program data from Brock and stores it in the database.'''
        self.browser.open('https://brocku.ca/programs')
        programs_list = self.browser.page.find_all('div', attrs={
            'class': 'content'
        })
        return self.read_programs(programs_list)

    def get(self):
        '''Gets programs from the chatbot database.'''

        # Pull club data from database
        programs = self.get_programs()

        # If database had no info, fetch new info
        if not programs:
            self.fetch()
            return self.get_programs()

        return programs

    def read_programs(self, programs_list):
        '''Extracts data from the list of programs.'''
        output = {}
        for index, program in enumerate(programs_list):
            self.browser.open(program.find('a', attrs={'class': 'readmore'}).get('href'))
            # Pull program information
            entry = {
                'name': self.get_name(program) or 'N/A',
                'description': self.get_description(self.browser.page) or 'N/A',
                'prerequisites': self.get_prerequisites(self.browser.page) or 'N/A'
            }

            output[index] = entry

        # Store info in the database
        self.store_programs(output)

        return output

    def get_name(self, program):
        '''Extracts the name from a program.'''
        try:
            return program.find('span').text
        except:
            return "N/A"

    def get_description(self, program):
        '''Extracts the name from a program.'''
        try:
            return program.find('div', attrs={
                'class': 'entry-content'
            }).text
        except:
            return "N/A"

    def get_prerequisites(self, program):
        '''Extracts the name from a program.'''
        try:
            return program.find('div', attrs={
                'class': 'col mid'
            }).text
        except:
            return "N/A"

    def store_programs(self, programs):
        '''Adds the programs to the database.'''
        with self.db_conn as conn:
            for index in programs:
                conn.execute(
                    '''
					INSERT OR REPLACE INTO programs 
					VALUES (?, ?, ?)
					''',
                    (
                        programs[index]['name'],
                        programs[index]['description'],
                        programs[index]['prerequisites']
                    )
                )
                conn.commit()

    def get_programs(self):
        '''Gets all the programs from the database and returns them as a dictionary.'''
        output = {}

        # Pull all programs from database
        with self.db_conn as conn:
            rows = conn.execute(
                '''
				SELECT *
				FROM programs
				'''
            ).fetchall()

        # Add programs to dictionary
        for index, row in enumerate(rows):
            output[index] = {
                'name': row['name'],
                'description': row['description'],
                'prerequisites': row['prerequisites']
            }

        return output
