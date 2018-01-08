#!flask/bin/python
from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Resource, Api

app = Flask(__name__)
mongo = PyMongo(app)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

