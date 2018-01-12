from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class Dao:
	def __init__(self):
		connection = MongoClient('mongo', 27017)
		self.db = connection['test']
		self.collection = self.db['students']

	def get_by_id(self, student_Id):
		student= self.collection.find_one({'_id': ObjectId(student_Id)})
		if student:
			return student
		return None

	def getStudents(self):
		students = self.collection.find()
		if not students:
			return []
		return students

	def delete(self, student_Id):
		deleted = self.collection.delete_one({'_id': ObjectId(student_Id)})
		return deleted
    
	def deleteAll(self):
		self.collection.remove({})
		return

	def update(self, student_Id, studentData):
		updatedStudent = self.collection.update_one({"_id": ObjectId(student_Id)}, {"$set": studentData}, upsert = False)
		return  ({"_id": student_Id, 'name': studentData['name']})

	def addStudent(self, studentData):
		Id = self.collection.insert_one(studentData).inserted_id
		if not Id:
			return None
		return {'_id': Id , 'name' : studentData['name'] }
		

