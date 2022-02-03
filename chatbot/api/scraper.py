import mechanicalsoup
import sqlite3

from apscheduler.schedulers.background import BackgroundScheduler


class Scraper:

	def __init__(self):
		self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
		self.db_conn.row_factory = sqlite3.Row
		self.browser = mechanicalsoup.StatefulBrowser()

		# Create database tables
		with self.db_conn as conn:
			conn.execute('CREATE TABLE IF NOT EXISTS clubs (name TEXT, contact TEXT, description TEXT)')

		self.setupScheduler()

	def setupScheduler(self):
		'''Runs functions in background_tasks at 12am every day.'''
		self.scheduler = BackgroundScheduler()
		self.background_tasks = [
			self.fetch_clubs
		]

		for job in self.background_tasks:
			self.scheduler.add_job(job, 'cron', hour=0, minute=0, timezone='EST')

		self.scheduler.start()

	def fetch_clubs(self):
		'''Fetches club data from Brock and stores it in the database.'''
		self.browser.open('https://www.brockbusu.ca/involvement/clubs/directory/')

		clubs_list = self.browser.page.find_all('li', attrs={'class': 'filterable-item'})
		output = {}

		def decodeEmail(e):
			'''
			Decrypts emails obfuscated by Cloudflare

			Author: sowa
			Source: https://stackoverflow.com/questions/36911296/scraping-of-protected-email
			'''
			de = ""
			k = int(e[:2], 16)

			for i in range(2, len(e)-1, 2):
				de += chr(int(e[i:i+2], 16)^k)

			return de

		for index, club in enumerate(clubs_list):
			club_name = club.find('h3').text
			club_contact = decodeEmail(club.find('span')['data-cfemail'])	

			# Check for clubs without descriptions
			try:
				club_description = club.find('p').text
			except AttributeError:
				club_description = None

			# Store data
			with self.db_conn as conn:
				conn.execute('''
					INSERT INTO clubs 
					VALUES (?, ?, ?)
					''', 
					(club_name, club_contact, club_description)
				)

			# Add data to output
			output[index] = {
				'name': club_name,
				'contact': club_contact,
				'description': club_description
			}

		return output

	def get_clubs(self):
		'''Gets clubs from the chatbot database.'''

		# Pull club data from database
		with self.db_conn as conn:
			rows = conn.execute(
				'''
				SELECT *
				FROM clubs
				'''
			).fetchall()
			
		# If there is no data in the database, fetch and try again
		if len(rows) == 0:
			self.fetch_clubs()
			return self.get_clubs()

		output = {}

		# Add data to output
		for index, row in enumerate(rows):
			output[index] =	{
				'name': row['name'],
				'contact': row['contact'],
				'description': row['description']
			}

		return output