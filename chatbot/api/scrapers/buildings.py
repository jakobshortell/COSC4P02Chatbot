import mechanicalsoup
import sqlite3
import pandas as pd


class BuildingScraper:

    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row

        # Create database tables
        with self.db_conn as conn:
            conn.execute(
                '''
				CREATE TABLE IF NOT EXISTS buildings (
					code TEXT, 
					name TEXT, 
					link TEXT,
					PRIMARY KEY (code)
				)
				'''
            )
            conn.commit()

    def fetch(self):
        '''Fetches buildings data from Brock and stores it in the database.'''
        self.browser.open('https://brocku.ca/blogs/campus-map/building-codes/')
        tables_list = self.browser.page.find_all('div', attrs={'class': 'entry-content'})
        list = str(tables_list[0])
        building_list = list.split('</p>')
        building_list.pop()
        return self.read_buildings(building_list)

    def get(self):
        '''Gets buildings from the chatbot database.'''
        # Pull club data from database
        buildings = self.get_buildings()
        # If database had no info, fetch new info
        if not buildings:
            self.fetch()
            return self.get_buildings()
        return buildings

    def read_buildings(self, buildings_list):
        '''Extracts data from the list of buildings.'''
        output = {}
        for index, buildings in enumerate(buildings_list):
            # Pull department information
            entry = {
                'code': self.get_name(buildings),
                'name': self.get_code(buildings),
                'link': self.get_link(buildings)
            }
            output[index] = entry
        # Store info in the database
        self.store_buildings(output)
        return output

    def get_code(self, buildings):
        '''Extracts the name from a buildings.'''
        try:
            i = buildings.find('<p>') + 3
            buildings = buildings[i : : ]
            return buildings
        except:
            return None

    def get_name(self, buildings):
        '''Extracts the code from a buildings.'''
        try:
            i = buildings.find('in ') + 3
            buildings = buildings[i::]
            i = buildings.find('">')
            buildings = buildings[:i:]
            return buildings
        except:
            return None

    def get_link(self, buildings):
        '''Extracts the link from a buildings.'''
        try:
            i = buildings.find('href="') + 6
            buildings = buildings[i::]
            i = buildings.find('" title')
            buildings = buildings[:i:]
            return buildings
        except:
            return None

    def store_buildings(self, buildings):
        '''Adds the buildings to the database.'''
        with self.db_conn as conn:
            for index in buildings:
                conn.execute(
                    '''
					INSERT OR REPLACE INTO buildings
					VALUES (?, ?, ?)
					''',
                    (
                        buildings[index]['code'],
                        buildings[index]['name'],
                        buildings[index]['link']
                    )
                )
                conn.commit()

    def get_buildings(self):
        '''Gets all the buildings from the database and returns them as a dictionary.'''
        output = {}

        # Pull all departments from database
        with self.db_conn as conn:
            rows = conn.execute(
                '''
				SELECT *
				FROM buildings
				'''
            ).fetchall()

        # Add departments to dictionary
        for index, row in enumerate(rows):
            output[index] = {
                'code': row['code'],
                'name': row['name'],
                'link': row['link']
            }

        return output
