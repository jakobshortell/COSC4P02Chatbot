from flask import Flask, request

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def main():
    request_data = request.get_json()
    user_message = request_data['userMessage']
    return {
        'content': user_message.upper()
    }


if __name__ == '__main__':
    app.run(debug=True)
