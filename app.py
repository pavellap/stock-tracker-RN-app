from flask import Flask, redirect, render_template, request
from flask_restful import Api, Resource, reqparse
from db import Table
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)


class Apitable(Resource):
    def get(self, id):
        try:
            return dumps(Table.find_one({'ID': id})), 200
        except:
            return "Line not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        values = parser.parse_args()
        line = {
            "Name": values["Name"]
        }
        try:
            line = dumps(Table.update({'ID': id}, {set: line}))
            return line, 201
        except:
            return f"Line with id {id} already exists", 400

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        values = parser.parse_args()
        if Table.find_one({'ID': id}):
            return f"Line with id {id} already exists", 400
        else:
            line = {
                "ID": id,
                "Name": values["Name"]
            }
            Table.insert_one(line)
            return f"Line with id {id} successfully inserted ", 201

    def delete(self, id):
        Table.delete_one({'ID': id})
        return f"Line with id {id} is deleted.", 200


api.add_resource(Apitable, "/api-table/<int:id>")
if __name__ == "__main__":
    app.run(debug=True)

