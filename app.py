from flask import Flask, redirect, render_template, request
from flask_restful import Api, Resource, reqparse
import random
from db import Table

app = Flask(__name__)
api = Api(app)

ai_quotes = [
    {
        "id": 0,
        "author": "Kevin Kelly",
        "quote": "The business plans of the next 10,000 startups are easy to forecast: " +
                 "Take X and add AI."
    },
    {
        "id": 1,
        "author": "Stephen Hawking",
        "quote": "The development of full artificial intelligence could " +
                 "spell the end of the human race… " +
                 "It would take off on its own, and re-design " +
                 "itself at an ever increasing rate. " +
                 "Humans, who are limited by slow biological evolution, " +
                 "couldn't compete, and would be superseded."
    },
    {
        "id": 2,
        "author": "Claude Shannon",
        "quote": "I visualize a time when we will be to robots what " +
                 "dogs are to humans, " +
                 "and I’m rooting for the machines."
    },
    {
        "id": 3,
        "author": "Elon Musk",
        "quote": "The pace of progress in artificial intelligence " +
                 "(I’m not referring to narrow AI) " +
                 "is incredibly fast. Unless you have direct " +
                 "exposure to groups like Deepmind, " +
                 "you have no idea how fast — it is growing " +
                 "at a pace close to exponential. " +
                 "The risk of something seriously dangerous " +
                 "happening is in the five-year timeframe." +
                 "10 years at most."
    },
    {
        "id": 4,
        "author": "Geoffrey Hinton",
        "quote": "I have always been convinced that the only way " +
                 "to get artificial intelligence to work " +
                 "is to do the computation in a way similar to the human brain. " +
                 "That is the goal I have been pursuing. We are making progress, " +
                 "though we still have lots to learn about " +
                 "how the brain actually works."
    },
    {
        "id": 5,
        "author": "Pedro Domingos",
        "quote": "People worry that computers will " +
                 "get too smart and take over the world, " +
                 "but the real problem is that they're too stupid " +
                 "and they've already taken over the world."
    },
    {
        "id": 6,
        "author": "Alan Turing",
        "quote": "It seems probable that once the machine thinking " +
                 "method had started, it would not take long " +
                 "to outstrip our feeble powers… " +
                 "They would be able to converse " +
                 "with each other to sharpen their wits. " +
                 "At some stage therefore, we should " +
                 "have to expect the machines to take control."
    },
    {
        "id": 7,
        "author": "Ray Kurzweil",
        "quote": "Artificial intelligence will reach " +
                 "human levels by around 2029. " +
                 "Follow that out further to, say, 2045, " +
                 "we will have multiplied the intelligence, " +
                 "the human biological machine intelligence " +
                 "of our civilization a billion-fold."
    },
    {
        "id": 8,
        "author": "Sebastian Thrun",
        "quote": "Nobody phrases it this way, but I think " +
                 "that artificial intelligence " +
                 "is almost a humanities discipline. It's really an attempt " +
                 "to understand human intelligence and human cognition."
    },
    {
        "id": 9,
        "author": "Andrew Ng",
        "quote": "We're making this analogy that AI is the new electricity." +
                 "Electricity transformed industries: agriculture, " +
                 "transportation, communication, manufacturing."
    }
]


class Quote(Resource):
    def get(self, id):
        try:
            return Table.find_one({'ID': id}), 200
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
            Table.update({'ID': id}, {set: line})
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
            return line, 201

    def delete(self, id):
        Table.delete_one({'ID': id})
        return f"Quote with id {id} is deleted.", 200


api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
if __name__ == "__main__":
    app.run(debug=True)
