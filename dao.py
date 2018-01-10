from pymongo import MongoClient
from pymongo import ObjectId

class Dao:
    def __init__(self):
         connection = MongoClient('localhost', 27017)
         self.db = self.connection['test']
         self.collection = self.db['students']

    def get_by_id(self, student_Id):
       	student= self.collection.find_one({'_id': ObjectId(student_Id)})
	if student is not None:
		return student
        return None
		
    def getStudents(self):
        return self.collection

    def delete(self, student_Id):
        student = self.collection.find_one({'_id:': ObjectId(student_Id)})
        if not student:
            	return None
        try:
		deleted = self.collection.delete_one({"_id": ObjectId(student_Id)})
        except:
		raise
	return deleted

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

 
