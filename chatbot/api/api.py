from flask import Flask, request
from random import seed
from random import randint
import sys
import json

app = Flask(__name__)


@app.route('/api', methods=["POST","GET"])
def main():
    message = request.get_json()
    stringmessage = str(message)
    print (stringmessage)
    if stringmessage=="None":
        return {"content":"This is a test response. For testing purposes."}
    return {"content":stringmessage.upper()}


if __name__ == '__main__':
    app.run(debug=True)
