import mechanicalsoup
import sqlite3

class ClubScraper:

	def __init__(self):
		self.browser = mechanicalsoup.StatefulBrowser()
		self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
		self.db_conn.row_factory = sqlite3.Row

		# Create database tables
		with self.db_conn as conn:
			conn.execute(
				'''
				CREATE TABLE IF NOT EXISTS clubs (
					name TEXT, 
					email TEXT, 
					description TEXT
				)
				'''
			)

	def fetch(self):
		'''Fetches club data from Brock and stores it in the database.'''
		self.browser.open('https://www.brockbusu.ca/involvement/clubs/directory/')

		# Get all clubs and read them into the database
		clubs_list = self.browser.page.find_all('li', attrs={
			'class': 'filterable-item'
		})
		return self.read_clubs(clubs_list)

	def get(self):
		'''Gets clubs from the chatbot database.'''

		# Pull club data from database
		clubs = self.get_clubs()

		# If database had no info, fetch new info
		if not clubs:
			self.fetch()
			return self.get_clubs()

		return clubs

	def decodeEmail(self, e):
		'''
		Decrypts emails obfuscated by Cloudflare

		Author: sowa
		Source: https://stackoverflow.com/questions/36911296/scraping-of-protected-email
		'''
		de = ""
		k = int(e[:2], 16)

		for i in range(2, len(e) - 1, 2):
			de += chr(int(e[i:i + 2], 16) ^ k)

		return de

	def read_clubs(self, clubs_list):
		'''Extracts data from the list of clubs.'''
		output = {}

		for index, club in enumerate(clubs_list):

			# Pull club information
			entry = {
				'name': self.get_name(club),
				'email': self.get_email(club),
				'description': self.get_description(club)
			}

			output[index] = entry

		# Store info in the database
		self.store_clubs(output)

		return output

	def get_name(self, club):
		'''Extracts the name from a club.'''
		return club.find('h3').text

	def get_email(self, club):
		'''Extracts the email from a club.'''
		return self.decodeEmail(club.find('span')['data-cfemail'])

	def get_description(self, club):
		'''Extracts the description from a club.'''
		try:
			club_description = club.find('p').text
		except AttributeError:
			club_description = None

		return club_description

	def store_clubs(self, clubs):
		'''Adds the club to the database.'''
		with self.db_conn as conn:
			for index in clubs:
				conn.execute('''
					INSERT INTO clubs 
					VALUES (?, ?, ?)
					''', 
					(
						clubs[index]['name'], 
						clubs[index]['email'], 
						clubs[index]['description']
					)
				)

	def get_clubs(self):
		'''Gets all the clubs from the database and returns them as a dictionary.'''
		output = {}

		# Pull all clubs from database
		with self.db_conn as conn:
			rows = conn.execute(
				'''
				SELECT *
				FROM clubs
				'''
			).fetchall()

		# Add clubs to dictionary
		for index, row in enumerate(rows):
			output[index] = {
				'name': row['name'],
				'email': row['email'],
				'description': row['description']
			}

		return output
