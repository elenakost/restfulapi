from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request, abort
from model import Model
from validator import validator, MultipleInvalid
import json
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')

class Student(Resource):
    def get(self, student_id):
        try:
            validator.validateId(student_id)
            student = Model.get_by_id(student_id) 
        except MultipleInvalid as e:
            return str(e), 400
        except:
           return 'error', 500
        if not student:
            abort(404, message = "Getting Student {} failed".format(student_id))
        _return = jsonify(student.__dict__)
        _return.status_code = 200
        return _return      
        
        
    def delete(self, student_id):
        try:
            validator.validateId(student_id)
            deleted = Model.delete(student_id)          
        except MultipleInvalid as e:
            return str(e), 400
        except:
            return 'error', 500
        if not deleted:
            abort(404, message = "Deleting Student {} failed".format(student_id))
        return '', 204
        
        
    def put(self, student_id):
        args = parser.parse_args()
        try:
            validator.validatePut(student_id, args['name'])
            student = Model.update(student_id, args)          
        except MultipleInvalid as e:
            return str(e), 400
        except:
            return 'error', 500
        _return = jsonify(student.__dict__)
        _return.status_code = 201
        return _return    
    
class StudentList(Resource):
    def get(self):
        try:
            students = Model.getStudents() 
        except:
            return 'an error', 500
        if not students:
            abort(404, message = "Getting all Students failed")
        jsonlist = []
        for s in students:
            jsonlist.append(s.__dict__)
        return jsonlist, 200
        
        
    def post(self):
        args = parser.parse_args()
        try:
            validator.validateData(args['name'])
            student = Model.addStudent(args)        
        except MultipleInvalid as e:
            return str(e), 400
        except:
            return 'error', 500
        _return = jsonify(student.__dict__)
        _return.status_code = 201
        return _return    

    def delete(self):
        try:
            deleted = Model.deleteAll()
        except:
            return 'error', 500
        return 'deleted', 204

api.add_resource(StudentList, '/students')
api.add_resource(Student, '/students/<student_id>')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
