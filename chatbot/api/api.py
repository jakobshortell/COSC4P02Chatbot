from flask import Flask, request
from scraper import Scraper

app = Flask(__name__)
scraper = Scraper()


@app.route('/api', methods=['POST', 'GET'])
def main():
    '''The main enpoint for requests made to the chatbot.'''
    
    request_data = request.get_json()
    user_message = request_data['userMessage']

    response = {
        'content': 'I am sorry. I don\'t know what you are asking.'
    }

    if 'club' in user_message.lower():
        clubs = scraper.get_clubs()
        club_names = [clubs[i]['name'] for i in clubs]
        response['content'] = 'Here are all the clubs at Brock:\n\n' + ', '.join(club_names)

    return response

if __name__ == '__main__':
    app.run(debug=True)
