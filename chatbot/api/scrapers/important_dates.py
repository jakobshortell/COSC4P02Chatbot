import mechanicalsoup
import sqlite3
import pandas as pd

class ImportantDatesScraper:

    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row

        '''
        NOTE: The table rows for the table below dont matter since the table 
        gets overwritten by pandas. It just needs to exist for the sake of the 
        get method.
        '''

        # Create database tables
        with self.db_conn as conn:
            conn.execute(
                '''
				CREATE TABLE IF NOT EXISTS dates (
                    placeholder TEXT
                )
				'''
            )
            conn.commit()

    def fetch(self):
        '''Fetches important dates from Brock and stores it in the database.'''
        tables_list = pd.read_html('https://brocku.ca/important-dates')

        # Only store fall/winter, spring, and summer tables
        self.store_tables(tables_list[:3])

        return self.get()

    def get(self):
        '''Gets dates from the chatbot database.'''

        # Pull import date data from database
        dates = self.get_dates()

        # If database had no info, fetch new info
        if not dates:
            self.fetch()
            return self.get_dates()

        return dates

    def store_tables(self, tables):
        '''Reads the contents of each table and stores it in the database.'''

        # Combine tables into a data frame
        column_names = ['Occasion', 'Session', 'Stakeholder/Type', 'Date']
        frames = [pd.DataFrame(table, columns=column_names) for table in tables]
        frame = pd.concat(frames)

        # Insert contents of data frame into database
        with self.db_conn as conn:
            frame.to_sql('dates', conn, if_exists='replace', index=False)

    def get_dates(self):
        '''Gets all the dates from the database and returns them as a dictionary.'''
        output = {}

        # Pull all dates from database
        with self.db_conn as conn:
            rows = conn.execute(
                '''
				SELECT *
				FROM dates
				'''
            ).fetchall()

        # Add dates to dictionary
        for index, row in enumerate(rows):
            output[index] = {
                'occasion': row['Occasion'],
                'session': row['Session'],
                'stakeholder/type': row['Stakeholder/Type'],
                'date': row['Date']
            }

        return output
