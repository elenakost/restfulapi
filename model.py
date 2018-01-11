from dao import Dao
import sys
class Model:
  
    def __init__(self, collection):
        self._id = str(collection['_id'])
        self.name = collection['name']
        

    @staticmethod
    def get_by_id(student_Id):
        dao = Dao()
        try:
          student = dao.get_by_id(student_Id)
        except:
          return None
        if student:
            
            return Model(student)
        else:
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
        dao.deleteAll()
        return
        
    @staticmethod
    def delete(student_Id):
        dao = Dao()
        try:
          deleted=dao.delete(student_Id)
          return Model(deleted)
        except:    
          return None

    @staticmethod
    def getStudents():
        dao = Dao()
        allstud = dao.getStudents()
        students = []
        for s in allstud.find():
            print (s,file=sys.stderr)
            students.append(repr(Model(s)))
        return str(students)

   



