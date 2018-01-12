import Dao
class Model:
  
    def __init__(self, collection):
        self._id = str(collection['_id']) if '_id' in collection else None
        self.name = collection['name']      

    @staticmethod
    def get_by_id(student_Id):
        dao = Dao()
        student = dao.get_by_id(student_Id)
        if not student:
            return None
        return Model(student)
           
    @staticmethod
    def addStudent(studentInfo):
        dao = Dao()
        new= dao.addStudent(studentInfo)
        if not new:
          return None
        return Model(new)

    @staticmethod
    def update(student_Id, studentInfo):
        dao = Dao()
        updated = dao.update(student_Id, studentInfo)
        if not updated:
          return None
        return Model(updated)

    @staticmethod
    def deleteAll():
        dao=Dao()
        dao.deleteAll()
        return
        
    @staticmethod
    def delete(student_Id):
        dao = Dao()
        deleted=dao.delete(student_Id)
        return deleted

    @staticmethod
    def getStudents():
        dao = Dao()
        allstud = dao.getStudents()
        students = []
        for s in allstud:
            students.append(Model(s))
        return students

