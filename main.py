import logging
import os
from flask import Flask,  request
from Helper.db_functions import client, user

app = Flask(__name__)
APP_ROUTE = os.path.dirname(os.path.abspath(__file__))
@app.route("/client", methods = ['GET'])
def get_client_info():
    data = client().query_client()
    return data


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)