import requests

class brockNewsScraper:

    def get(self):
        rss = requests.get("https://brocku.ca/brock-news/feed/")
        title_list = rss.text
        cnt = title_list.count('<title>')
        link_list = rss.text
        msg = 'Here is the latest Brock News:\n'
        for x in range(cnt):
            i = title_list.find('<title>') + 7
            title_list = title_list[i::]
            i = title_list.find('</title>')
            title = title_list[:i:]
            i = link_list.find('<link>') + 6
            link_list = link_list[i::]
            i = link_list.find('</link>')
            link = link_list[:i:]
            msg = msg + "• " + title + ": " + link + "\n"
        return msg
