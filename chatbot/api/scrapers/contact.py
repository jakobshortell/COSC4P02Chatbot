import requests
import sqlite3
from requests_html import HTMLSession


class ContactScraper:

    def __init__(self):
        self.session = HTMLSession()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row

        # Create database tables
        with self.db_conn as conn:
            conn.execute(
                '''
				CREATE TABLE IF NOT EXISTS contacts (
				    department TEXT,
					name TEXT, 
                    email TEXT,
					title TEXT, 
					phone TEXT,
					location TEXT,
					PRIMARY KEY (name)
				)
				'''
            )
            conn.commit()

    def fetch(self):
        '''Fetches contacts from Brock and stores it in the database.'''
        contact_codes = self.fetch_contact_codes()
        output = {}

        for con in contact_codes:
            output[con] = self.fetch_contacts(con)

        return output

    def get(self):
        '''Gets contacts from the chatbot database.'''
        output = {}
        output = self.get_contacts()
        # If program codes is empty, fetch hasn't been run
        # if not self.program_codes:
        #    self.fetch()
        #   return self.get()

        return output

    def fetch_contact_codes(self):
        '''Returns a list of all the contact codes from Brock University.'''
        response = self.session.get("https://brocku.ca/directory/")
        contact_num = response.text
        contact_list = []
        while (True):
            if (contact_num.find('<option value=') != -1):
                i = contact_num.find('<option value=') + 15
                contact_num = contact_num[i::]
                i = contact_num.find('::')
                contact_list.append(contact_num[:i:])
            else:
                break
        contact_list.pop(0)
        response.close()
        return contact_list

    def fetch_contacts(self, code):
        '''Returns a dictionary containing all contacts at Brock University.'''
        response = self.session.get("http://brocku.ca/directory/?department=" + code)
        response.html.render(sleep=3, timeout=15)
        table = response.html.find('tr')
        cnt = len(table) - 7
        # scraps each row
        department = response.html.find('td.department')
        first_name = response.html.find('td.firstname')
        last_name = response.html.find('td.lastname')
        email = response.html.find('td.email')
        title = response.html.find('td.title')
        phone = response.html.find('td.extension')
        location = response.html.find('td.location')
        contacts = {}
        # Loop through the rows
        try:
            for index in range(cnt):
                contacts[index] = {
                    'department': department[index].text,
                    'name': first_name[index].text + ' ' + last_name[index].text,
                    'email': email[index].text,
                    'title': title[index].text,
                    'phone': "(905) 688-5550 x" + phone[index].text[4::],
                    'location': location[index].text
                }
            # Store contacts in the database
            self.store_contacts(contacts)
        except:
            None

        response.close()
        return contacts

    def store_contacts(self, contacts):
        '''Adds contacts to the database.'''
        with self.db_conn as conn:
            for index in contacts:
                conn.execute(
                    '''
					INSERT OR REPLACE INTO contacts 
					VALUES (?, ?, ?, ?, ?, ?)
					''',
                    (
                        contacts[index]['department'],
                        contacts[index]['name'],
                        contacts[index]['email'],
                        contacts[index]['title'],
                        contacts[index]['phone'],
                        contacts[index]['location']
                    )
                )
                conn.commit()



    def get_contacts(self):
        '''Gets all the contacts from the database and returns them as a dictionary.'''
        output = {}

        # Pulls all contacts from the database
        with self.db_conn as conn:
            rows = conn.execute(
                '''
                SELECT *
                FROM contacts
                '''
            ).fetchall()

        # Add courses to dictionary
        for index, row in enumerate(rows):
            output[index] = {
                'department': row['department'],
                'name': row['name'],
                'email': row['email'],
                'title': row['title'],
                'phone': row['phone'],
                'location': row['location']
            }

        return output

#s = ContactScraper()
#s.fetch()
