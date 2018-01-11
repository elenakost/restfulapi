from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

class Dao:
	def __init__(self):
		connection = MongoClient('localhost', 27017)
		self.db = connection['test']
		self.collection = self.db['students']

	def get_by_id(self, student_Id):
                student= self.collection.find_one({'_id': ObjectId(student_Id)})
                if student:
                        return student
                return None

	def getStudents(self):
		print("dao",file=sys.stderr)
		return self.collection

	def delete(self, student_Id):
                try:
                        student= self.collection.find_one({'_id': ObjectId(student_Id)})
                        deleted = self.collection.delete_one({'_id': ObjectId(student_Id)})
                except:
                        raise
                if student:
                        return student
                return None
    
	def deleteAll(self):
        	self.collection.remove({})
        	return

	def update(self, student_Id, studentData):
		try:
			updatedStudent = self.collection.update_one({"_id": ObjectId(student_Id)}, {"$set": studentData}, upsert = False)
			student = self.collection.find_one({'_id': ObjectId(student_Id)})
		except:
			raise
		if not student:
			return None
		return student

	def addStudent(self, studentData):
		try:
			Id = self.collection.insert_one(studentData).inserted_id
		except:
			raise
		if Id is not None:
			return self.collection.find_one({"_id": Id.inserted_id})
		return None

 
