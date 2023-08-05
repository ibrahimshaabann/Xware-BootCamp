from Parent1 import Parent

class Student (Parent):
    def __init__(self, id = None, name = None, age = None, stuDepartment = None):
        self.stuDepartment = stuDepartment
        super().__init__(id, name, age)