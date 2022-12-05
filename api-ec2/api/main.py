from flask import Flask, jsonify, request, json
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from status_ec2 import status
from start_ec2 import start
from stop_ec2 import stop

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

@app.route('/statusEC2/<string:id>', methods=['GET'])
def verify_status_instance(id):
    return status(id)

@app.route('/startEC2/<string:id>', methods=['POST'])
def start_ec2_instance(id):
    return start(id)

@app.route('/stopEC2/<string:id>', methods=['POST'])
def stop_ec2_instance(id):
    return stop(id)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
