from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)
api = Api(app)


USERS = {
    'user1': {'name': 'elena'},
    'user2': {'name': 'bob'},
}

def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="User {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('name')

class Users(Resource):
    def get(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        return USERS[user_id]

    def delete(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        del USERS[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        n= {'name': args['name']}
        USERS[user_id] = n
        return n, 201

class UsersList(Resource):
    def get(self):
        return USERS
    #not working, telling me post is an invalid method  
    def post(self):
        args = parser.parse_args()
        user = int(max(USERS.keys()).lstrip('user')) + 1
        user_id = 'user%(user)' % {"user"}
        USERS[user_id] = {'name': args['name']}
        return USERS[user_id], 201

#not sure what these 2 lines do
api.add_resource(UsersList, '/users')
api.add_resource(Users, '/users/<user_id>')


if __name__ == '__main__':
    app.run(debug=True)
