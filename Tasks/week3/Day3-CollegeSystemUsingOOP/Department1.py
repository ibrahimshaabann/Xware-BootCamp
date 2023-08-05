from BaseModel1 import BaseModel
from Faculty1 import facultiesList , Faculty
import os

'''
    Department has a set of (set data structure) subjects->>>> its an aggregation relationship
    sdgsdg
    dfhgdfh

'''
class Department(BaseModel):
    def __init__(self,id = None, name = None, subjectsSet = None) :
        self.subjects = subjectsSet
        super().__init__(id, name)

    @staticmethod
    def addDepartments ():
        '''
            Add departments to faculty object
        '''
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Add Departments \n\n")
        searchId = input("\n\n\n\t\tPlease Enter Faculty Id: ")
        facObjectToAddDepartmentsInto = Faculty()
                        
        for fac in facultiesList:
            
            if fac.id == searchId:   
                facObjectToAddDepartmentsInto = fac             
                print(fac.description())
                break

        # if the facObjectToAddDepartmentsInto still none as before, that means that the id was non found
        if facObjectToAddDepartmentsInto == None: 
            raise ValueError("Ths faculty Id doesn't exist!!")
           
        noOfDeps = int(input("\n\n\n\t\tPlease enter number of departments you wanna add: "))

        for count in range (noOfDeps):
            depId = input(f"\n\n\t\tPlease Enter department {count + 1} Id: ")
            depname = input(f"\n\n\t\tPlease Enter department {count + 1} name: ")       
            facObjectToAddDepartmentsInto.departmentsSet.add(Department (depId, depname)) # Create dep object in faculty object departments set


        print(f"\n\n\n\t\tDepartments Added to {facObjectToAddDepartmentsInto.name} Faculty: ",end="")

        # Loop to print departments in the faculty object
        for dep in  (facObjectToAddDepartmentsInto.departmentsSet):     
            print(f" {dep.name}" , end= " ")

        enter = input("\n\n\t\t- Press any button to getback to the Main Menu")
        os.system('clear')    

        def description(self):
            return super().description 




   