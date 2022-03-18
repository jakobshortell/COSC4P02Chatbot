import feedparser

class eventScraper:

    def get(self):
        NewsFeed = feedparser.parse("https://www.niagarathisweek.com/rss/event/")
        event_list = NewsFeed.entries
        msg = 'Here are some of the events going on around the Niagara region:\n'
        for i in event_list:
            msg = msg + i.title + ': ' + i.link + '\n'
        return msg