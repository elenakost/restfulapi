from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request
from model import Model
from voluptuous.voluptuous.schema_builder import Schema, Required
from voluptuous.voluptuous.validators import Length, All, MultipleInvalid

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')

idSchema = Schema(All(str, Length(min=24, max=24)))
jsSchema=Schema(str)

class Student(Resource):
    def get(self, student_id):
        try:
            if(idSchema(student_id)==student_id):
                student=Model.get_by_id(student_id)
            else:
                raise AssertionError('MultipleInvalid not raised')
        except MultipleInvalid as e:
            exc = e
            print (str(exc))
        if student is None:
            abort(404, message="Getting Student {} failed".format(student_id))
        return student
        
    def delete(self, student_id):
        try:
            if(idSchema(student_id)==student_id):
                deleted = Model.delete(student_Id)
            else:
                raise AssertionError('MultipleInvalid not raised')           
        except MultipleInvalid as e:
            exc = e
            print (str(exc))
        if student is None:
            abort(404, message="Deleting Student {} failed".format(student_id))
        return '', 204
        
    def post(self):
        args = parser.parse_args()
        try:
            if(jsSchema(args['name'])==args['name']):
                n= {'name': args['name']}
                student = Model.addStudent(n)
            else:
                raise AssertionError('MultipleInvalid not raised')           
        except MultipleInvalid as e:
            exc = e
            print (str(exc))
        return student, 201
        
    def put(self, student_id):
        args = parser.parse_args()
        try:
            if(jsSchema(args['name'])==args['name'] && idSchema(student_id)==student_id)):
                n= {'name': args['name']}
                student = Model.update(student_Id, n)
            else:
                raise AssertionError('MultipleInvalid not raised')           
        except MultipleInvalid as e:
            exc = e
            print (str(exc))
        return student, 201
    
class StudentList(Resource):
    def get(self):
        try:
            students = Model.getStudents() 
        except:
            print("an error")
        if students is None:
            abort(404, message="Getting all Students {} failed".format(student_id))
        return students
        
    def post(self):
        args = parser.parse_args()
        try:
            if(jsSchema(args['name'])==args['name']):
                n= {'name': args['name']}
                student = Model.addStudent(n)
            else:
                raise AssertionError('MultipleInvalid not raised')           
        except MultipleInvalid as e:
            exc = e
            print (str(exc))
        return student, 201

     def delete(self, student_id):
        try:
            if(idSchema(student_id)==student_id):
                deleted = Model.deleteAll(student_Id)
            else:
                raise AssertionError('MultipleInvalid not raised')
        except MultipleInvalid as e:
            exc = e
            print (str(exc))
        if deleted is None:
            abort(404, message="Deleting Students {} failed".format(student_id))
        return '', 204

api.add_resource(StudentList, '/students')
api.add_resource(Students, '/students/<student_id>')

if __name__ == '__main__':
    app.run(debug=True)
