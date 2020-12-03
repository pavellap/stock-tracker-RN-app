from flask import Flask, redirect, render_template, request
from flask_restful import Api, Resource, reqparse
from db import Table
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)


class Info_short(Resource):
    def get(self, limit):
        try:
            return dumps(Table.find().limit(limit)), 200
        except:
            return "Position not found", 404


class Info_long(Resource):
    def get(self, ticker):
        try:
            return dumps(Table.find_one({'ticker': ticker})), 200
        except:
            return "Position not found", 404


api.add_resource(Info_short, "/info-short/<int:limit>")
api.add_resource(Info_long, "/info-long/<string:ticker>")
if __name__ == "__main__":
    app.run(debug=True)

