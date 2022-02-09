from apscheduler.schedulers.background import BackgroundScheduler

class ScrapeScheduler:
	
	def __init__(self, scrapers={}):

		self._scrapers = {}

		if scrapers:
			self._scheduler = BackgroundScheduler()

			for name, scraper in scrapers.items():
				self._scrapers[name] = scraper
				self._scheduler.add_job(scraper.fetch, 'cron', hour=0, minute=0, timezone='EST')

			self._scheduler.start()

	def get_scrapers(self):
		return self._scrapers