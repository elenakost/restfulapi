from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request
from model import Model

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')

class Student(Resource):
    def get(self, student_id):
        try:
            if ObjectId.is_valid(id):
                student=Model.get_by_id(student_id)
        except:
            return '',500
        if student is None:
            abort(404, message="Getting Student {} failed".format(student_id))
        return student
        
    def delete(self, student_id):
        try:
            if ObjectId.is_valid(id):
                deleted = Model.delete(student_Id)
        except:
            return '',500
        if student is None:
            abort(404, message="Deleting Student {} failed".format(student_id))
        return '', 204
        
    def post(self):
        args = parser.parse_args()
        try:
            n= {'name': args['name']}
            student = Model.addStudent(n)
        except KeyError:
            return #an error
        return student, 201
        
    def put(self, user_id):
        args = parser.parse_args()
        try:
            n= {'name': args['name']}
            student = Model.update(student_Id, n)
        except KeyError:
            return #an error
        return student, 201
    
class StudentList(Resource):
    def get(self):
        try:
            students = Model.getAllStudents() #not implemented yet
        except:
             return #an error
        if students is None:
            abort(404, message="Getting all Students {} failed".format(student_id))
        return students
        
    def post(self):
        args = parser.parse_args()
        try:
            n={'name': args['name']}
            student = Model.addStudent(n)
        except:
             return #an error
        return student, 201

     def delete(self, student_id):
        try:
            if ObjectId.is_valid(id):
                deleted = Model.deleteAll(student_Id)
        except:
            return #an error
        if deleted is None:
            abort(404, message="Deleting Students {} failed".format(student_id))
        return '', 204

api.add_resource(StudentList, '/students')
api.add_resource(Students, '/students/<student_id>')

if __name__ == '__main__':
    app.run(debug=True)