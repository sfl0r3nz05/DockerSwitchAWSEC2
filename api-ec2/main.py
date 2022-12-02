from flask import Flask, jsonify, request, json
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from filter import filter

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

class postNodesLinks(Resource):
    def post(self):
        return filter(request.json)


api.add_resource(postNodesLinks, '/sendnodelink')

if __name__ == '__main__':
    app.run(host="0.0.0.0")

