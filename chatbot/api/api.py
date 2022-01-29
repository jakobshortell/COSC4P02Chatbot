from flask import Flask
from scraper import Scraper

app = Flask(__name__)
scraper = Scraper()

@app.route('/api')
def main():
    return scraper.get_clubs()

if __name__ == '__main__':
    app.run(debug=True)