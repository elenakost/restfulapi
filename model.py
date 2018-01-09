from dao import Dao

collName='students'

class Model:

    #def save
    #def get_by_params
  
    def __init__(self, collection):
        self.id = collection['id'] if 'id' in collection else None

    @staticmethod
    def get_by_id(student_Id):
        dao = Dao()
        try:
          student = dao.get_by_id(student_Id)
          return Model(student)
        except:
          return None
        
    @staticmethod
    def addStudent(studentInfo):
        dao = Dao()
        try:
          new= dao.addStudent(studentInfo)
          return Model(new)
        except:
          return None
        

    @staticmethod
    def update(student_Id, studentInfo):
        dao = Dao()
        try:
          updated = dao.update(student_Id, studentInfo)
          return Model(updated)
        except:
          return None

    @staticmethod
    def deleteAll():
        dao=Dao()
        try:
          dao.deleteAll()
          return 
        except:
          return
        
    @staticmethod
    def deleteStudent(student_Id):
        dao = Dao()
        try:
          deleted=dao.delete(student_Id)
          return Model(deleted)
        except:    
          return None

