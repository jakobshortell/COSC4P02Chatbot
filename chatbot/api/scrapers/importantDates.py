import mechanicalsoup
import sqlite3
import pandas as pd



class ImportantDatesScraper:


	def __init__(self):
		self.browser = mechanicalsoup.StatefulBrowser()
		self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
		self.db_conn.row_factory = sqlite3.Row

		# Create database tables
		with self.db_conn as conn:
			conn.execute(
				'''
				CREATE TABLE IF NOT EXISTS dates (
					Occasion TEXT, 
					Session TEXT, 
					Type TEXT,
					Date TEXT,
					PRIMARY KEY (Occasion)
				)
				'''
			)
			conn.commit()

	def fetch(self):
		'''Fetches important dates from Brock and stores it in the database.'''
		dates_list = pd.read_html("https://brocku.ca/important-dates#fall-winter")

		return self.read_dates(dates_list[0])

	def get(self):
		'''Gets dates from the chatbot database.'''

		# Pull club data from database
		dates = self.get_dates()

		# If database had no info, fetch new info
		if not dates:
			self.fetch()
			return self.get_dates()

		return dates

	def read_dates(self, dates_list):
		output = pd.DataFrame(dates_list, columns= ['Occasion','Session', 'Stakeholder/Type', 'Date'])


		# Store info in the database
		self.store_dates(output)
		return output

	
	
	def store_dates(self, dates):
		'''Adds the clubs to the database.'''
		with self.db_conn as conn:
			dates.to_sql('dates', conn, if_exists='replace', index=False)

	def get_dates(self):
		'''Gets all the dates from the database and returns them as a dictionary.'''
		output = {}

		# Pull all departments from database
		with self.db_conn as conn:
			rows = conn.execute(
				'''
				SELECT *
				FROM dates
				'''
			).fetchall()

		# Add departments to dictionary
		for index, row in enumerate(rows):
			output[index] = {
				'Occasion': row['Occasion'],
				'Session': row['Session'],
				'Stakeholder/Type': row['Stakeholder/Type'],
				'Date': row['Date']
			}

		return output