from BaseModel1 import BaseModel

class Subject(BaseModel):
    def __init__ (self, id = None, name = None):
        super().__init__(id, name)