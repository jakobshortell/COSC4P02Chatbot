from flask import Flask, request

from scrapers.scheduler import ScrapeScheduler
from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
from scrapers.importantDates import ImportantDatesScraper

app = Flask(__name__)

# Instantiate scheduler and pass in instances of scrapers
scheduler = ScrapeScheduler(scrapers={
    'clubs': ClubScraper(),
    'departments': DepartmentScraper(),
    'dates' : ImportantDatesScraper()
})
scrapers = scheduler.get_scrapers()


@app.route('/api', methods=['POST', 'GET'])
def main():
    '''The main enpoint for requests made to the chatbot.'''
    request_data = request.get_json()
    user_message = request_data['userMessage']

    response = {
        'content': 'I am sorry. I don\'t know what you are asking.'
    }

    # Print an attribute of the first element in the response as a test
    if 'club' in user_message.lower():
        clubs = scrapers['clubs'].get()
        response['content'] = clubs[0]['name']

    elif 'department' in user_message.lower():
        departments = scrapers['departments'].get()
        response['content'] = departments[0]['name']

    elif 'dates' in user_message.lower():
        dates = scrapers['dates'].get()
        response['content'] = dates[0]['session']

    return response

if __name__ == '__main__':
    app.run(debug=True)
