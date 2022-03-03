from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
from scrapers.important_dates import ImportantDatesScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper

scrapers = [
	ClubScraper(),
	DepartmentScraper(),
	ImportantDatesScraper(),
	CoursesScraper(),
	ProgramScraper()
]

def run_scrapers():
	'''Runs the fetch() method on all scrapers.'''

	total = len(scrapers)

	# Loop through scrapers and fetch
	for index, scraper in enumerate(scrapers):
		print(f'[{index + 1}/{total}]', 'Fetching... ', end='')

		try:
			scraper.fetch()
		except Exception as e:
			raise e
		finally:
			print('Done.')

	print(f'Fetching completed.')

if __name__ == '__main__':
	run_scrapers()