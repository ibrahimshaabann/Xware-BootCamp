from BaseModel1  import BaseModel
from Professor1  import  Professor 

# Each course has a professor ----------> Aggregation
class Course(BaseModel):
     
    def __init__ (self, id, name = None, ProfReference = None, duration = None): 
        self.ProfReference = ProfReference
        super().__init__(id, name)