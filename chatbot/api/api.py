from flask import Flask, request

from scrapers.scheduler import ScrapeScheduler
from scrapers.clubs import ClubScraper

app = Flask(__name__)

# Instantiate scheduler and pass in instances of scrapers
scheduler = ScrapeScheduler(scrapers={
    'clubs': ClubScraper()
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

    if 'club' in user_message.lower():
        clubs = scrapers['clubs'].get()
        club_names = [clubs[i]['name'] for i in clubs]
        response['content'] = 'Here are all the clubs at Brock:\n\n' + ', '.join(club_names)

    return response

if __name__ == '__main__':
    app.run(debug=True)
