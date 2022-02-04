from flask import Flask, request
from scraper import Scraper

app = Flask(__name__)
scraper = Scraper()


@app.route('/api', methods=['POST'])
def main():
    request_data = request.get_json()
    user_message = request_data['userMessage']
    return {
        'content': scraper.get_clubs()
    }


if __name__ == '__main__':
    app.run(debug=True)
