from codecs import ignore_errors
from tkinter import E
from tokenize import Ignore
import mechanicalsoup
import sqlite3
from bs4 import BeautifulSoup


class TransportationScraper:

    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row

        # Create database tables
        with self.db_conn as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS transportation (
                    name TEXT, 
                    description TEXT,
                    link TEXT,
                    PRIMARY KEY (name)
                )
                '''
            )
            conn.commit()

    def fetch(self):
        '''Fetches transportation data from Brock and stores it in the database.'''
        self.browser.open('https://www.brockbusu.ca/services/transit/')
        # Get all transportation and read them into the database
        names_list = self.browser.page.find_all('ul', attrs={
            'class': 'x-nav x-nav-tabs four-up top'
        })
        desc_list = self.browser.page.find_all('div', attrs={
            'class': 'x-tab-content'
        })
        links_list = self.browser.page.find_all('div', attrs={
            'class': 'x-tab-content'
        })

        return self.read_transportation(names_list, desc_list, links_list)

    def get(self):
        '''Gets transportation from the chatbot database.'''

        # Pull transportation data from database
        transportation = self.get_transportation()

        # If database had no info, fetch new info
        if not transportation:
            self.fetch()
            return self.get_transportation()

        return transportation

    def read_transportation(self, name_list, desc_list, link_list):
        '''Extracts data from the list of transportation.'''
        output = {}
        names = []
        descs = []
        links = []

        for name in name_list[0]:
            names.append(self.get_name(name))

        for desc in desc_list[0]:
            descs.append(self.get_description(desc))

        for link in link_list[0]:
            links.append(self.get_link(link))

        for i in range(len(names)):
            entry = {
                'name': names[i],
                'description': descs[i],
                'link': links[i]
            }
            output[i] = entry

        self.store_transportation(output)

        return output

    def get_name(self, name):
        '''Extracts the name from transportation.'''
        try:
            return name.find('a').text
        except:
            return "N/A"

    def get_description(self, desc):
        '''Extracts the description from transportation.'''
        try:
            data = desc.contents[0]
            for d in data:
                try:
                    return d.text
                except:
                    return "N/A"

        except AttributeError:
            return "N/A"

    def get_link(self, link):
        '''Extracts the link from transportation.'''
        try:
            data = link.contents[2]
            # for d in data:
            try:
                soup = BeautifulSoup(str(link), 'lxml')
                for link in soup.findAll('a'):
                    return link.get('href')
            except:
                return "N/A"
        except AttributeError:
            return "N/A"

    def store_transportation(self, transportation):
        '''Adds the transportation to the database.'''
        with self.db_conn as conn:
            for index in transportation:
                conn.execute(
                    '''
                    INSERT OR REPLACE INTO transportation 
                    VALUES (?, ?, ?)
                    ''',
                    (
                        transportation[index]['name'],
                        transportation[index]['description'],
                        transportation[index]['link']
                    )
                )
                conn.commit()

    def get_transportation(self):
        '''Gets all the transportation from the database and returns them as a dictionary.'''
        output = {}

        # Pull all transportation from database
        with self.db_conn as conn:
            rows = conn.execute(
                '''
                SELECT *
                FROM transportation
                '''
            ).fetchall()

        # Add transportation to dictionary
        for index, row in enumerate(rows):
            output[index] = {
                'name': row['name'],
                'description': row['description'],
                'link': row['link']
            }

        return output

