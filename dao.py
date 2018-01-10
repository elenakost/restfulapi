from pymongo import MongoClient

class Dao:
    def __init__(self):
        table = '' 
        mongo = MongoClient('mongo')
        client = getattr(mongo, table)
        self.db = client
	      self.collection=self.db['students']

    def get_by_id(self, student_Id):
        try:
       	    student= self.collection.find_one({'_id': ObjectId(student_Id)})
        except:
            raise
	      if not student:
		       return None
        return student
		
    def getStudents(self):
        return self.collection

    def delete(self, student_Id):
        try:
		        deleted = self.collection.delete_one({'_id': ObjectId(student_Id)})
            student = self.collection.find_one({'_id': ObjectId(student_Id)})
        except:
		        raise
        if not student:
            return None
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
        else:
            return student

    def addStudent(self, studentData):
        try:
            Id = self.collection.insert_one(studentData).inserted_id
        except:
            raise
        if not Id:
            return None
        return self.collection.find_one({"_id": Id.inserted_id})


 
