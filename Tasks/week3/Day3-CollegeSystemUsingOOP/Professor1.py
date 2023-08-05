from Parent1 import Parent
from Faculty1 import facultiesList
from Faculty1 import Faculty


class Professor(Parent):
    def __init__ (self, id = None, firstName = None,surName = None, age = None, DepartmentName = None):
        self.DepartmentName = DepartmentName
        super().__init__(id, firstName, surName, age)



    @staticmethod
    def addProfessor(profObject, facSearchId):
        for fac in facultiesList :
            if facSearchId == fac.id:
                fac.profsList.append(profObject)
                print("\n\n\n\t\tProfessor Added successfully ")
                break

    @staticmethod
    def showProfessors(facSearchId):
        facultyObjReference = None
        for fac in facultiesList :
            if facSearchId == fac.id:
                facultyObjReference = fac

        for prof in facultyObjReference.profsList:
            print (f"\n\n\t\t\t {prof.description()}")
                


    def description(self):
        return super().description() + ", Deparment: " + self.DepartmentName