from Student1 import Student
from Course1 import Course
from BaseModel1 import BaseModel

# Student Enrolment has a student ------> Aggregation
# Student Enrolment has a course  ------> Aggregation
class StudentEnrolment(BaseModel):
    def __init__ (self, id = None, name = None, studentReference = None, courseRefernce = None):
        self.studentReference = studentReference
        self.courseRefernce = courseRefernce
        super().__init__(id, name)
