from BaseModel1 import BaseModel
class Parent :

    def __init__(self, id = None, firstName = None, surName = None, age = None):
        self.id = id
        self.firstName = firstName
        self.surName = surName
        self.age = age

    def description(self):
        return f"Profssor Id: {self.id}, Profssor Name: {self.firstName } {self.surName}, Profssor age: {self.age} "
