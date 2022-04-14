import requests
import mechanicalsoup
import sqlite3
import pandas as pd




class UnionScraper:

    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row

        with self.db_conn as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS restaurants (
                    name TEXT, 
                    description TEXT,
                    hour TEXT,
                    PRIMARY KEY (name)
                )
                '''
            )
            conn.commit()

    def fetch(self):
        self.browser.open('https://www.brockbusu.ca/businesses/union-station/')
        union_list = self.browser.page.find_all('div', attrs={'class': 'cs-content'})
        union = str(union_list)
        cnt = union.count('href="')
        link_list = []
        for x in range(cnt):
            temp = union
            i = temp.find('href="') + 6
            temp = temp[i::]
            union = temp
            i = temp.find('">View')
            temp = temp[:i:]
            link_list.append(temp)
        content = []
        link_list.append('https://www.brockbusu.ca/businesses/restaurant')
        link_list.append('https://www.brockbusu.ca/businesses/general-brock')
        for x in range(cnt+2):
            self.browser.open(link_list[x])
            content.append(self.browser.page.find_all('div', attrs={'class': 'x-container max width offset'}))
        return self.read_union(content)


    def read_union(self, content):
        output = {}

        for index, union in enumerate(content):
            # Pull department information
            entry = {
                'name': self.get_name(union),
                'description': self.get_description(union),
                'hour': self.get_hour(union)
            }

            output[index] = entry

        # Store info in the database
        self.store_union(output)

        return output


    def get_name(self, union):
        try:
            union = str(union)
            i = union.find('<h1 class="entry-title">') + 24
            union = union[i::]
            i = union.find('</h1>')
            union = union[:i:]
            return union
        except:
            return 'N/A'

    def get_description(self, union):
        try:
            union = str(union)
            i = union.find('<p>') + 3
            union = union[i::]
            i = union.find('</p>')
            union = union[:i:]
            union = union.replace('<br/>', '')
            return union
        except:
            return 'N/A'


    def get_hour(self, union):
        output= ''
        try:
            for x in range(5):
                temp = str(union)
                i = temp.find('<td><strong>') + 12
                temp = temp[i::]
                union = temp
                i = temp.find('</strong></td>')
                temp = temp[:i:]

                output = output + temp + " "
                temp = union
                i = temp.find('<td>') + 4
                temp = temp[i::]
                union = temp
                i = temp.find('</td>')
                temp = temp[:i:]
                if i == -1:
                    output = None
                else:
                    output = output + temp + "\n"

            return output

        except:
            return 'N/A'

    def store_union(self, union):
        with self.db_conn as conn:
            for index in union:
                conn.execute(
                    '''
                    INSERT OR REPLACE INTO restaurants
                    VALUES (?, ?, ?)
                    ''',
                    (
                        union[index]['name'],
                        union[index]['description'],
                        union[index]['hour']
                    )
                )
                conn.commit()
