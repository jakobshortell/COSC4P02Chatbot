from flask import Flask

app = Flask(__name__)

@app.route('/api')
def main():
    return {
        'content': 'This is a response from Flask!'
    }

if __name__ == '__main__':
    app.run(debug=True)