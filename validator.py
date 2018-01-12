from voluptuous.schema_builder import Schema, Required
from voluptuous.validators import Length, All, MultipleInvalid

class validator:
	idSchema = Schema(All(str, Length(min=24, max=24)))
	jsSchema=Schema(str)
		
	@classmethod
	def validateId(cls,sid):
		return cls.idSchema(sid)
	
  @classmethod
	def validatePut(cls,sid, data):
		cls.jsSchema(data)
		cls.idSchema(sid)
		return

	@classmethod
	def validateData(cls,data):
		cls.jsSchema(data)
		return
