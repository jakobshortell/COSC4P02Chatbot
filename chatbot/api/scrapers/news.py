import feedparser

class newsScraper:

    def get(self):
        NewsFeed = feedparser.parse("https://www.niagarathisweek.com/rss/article?category=news")
        event_list = NewsFeed.entries
        msg = 'Here are some of the news in the Niagara region:\n'
        for i in event_list:
            msg = msg + "• " + i.title + ': ' + i.link + '\n'
        return msg