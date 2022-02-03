from flask import Flask, request

app = Flask(__name__)


@app.route('/api', methods=['POST', 'GET'])
def main():
    message = request.get_json()
    stringmessage = str(message)

    if stringmessage=="None":
        return {
            'content': 'This is a test response. For testing purposes.'
        }

    return {
        'content': stringmessage.upper()
    }


if __name__ == '__main__':
    app.run(debug=True)
