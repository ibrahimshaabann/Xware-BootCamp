from BaseModel1 import BaseModel
import os

facultiesList = []

# Departments are part of faculty --------> it is a composition relationship
class Faculty(BaseModel):
    def __init__(self, id = None, name = None,  departmentsSet= set(), profsList = [] ):
        self.departmentsSet = departmentsSet
        self.profsList = profsList
        super().__init__(id, name)


    

    def createFaculty ():
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Create Faculty \n\n")
        Id = input("\n\n\n\t\tPlease Enter Faculty Id: ")
        name = input("\n\n\n\t\tPlease Enter Faculty Name: ")   
            
        try:
            facultyObj = Faculty(Id, name)
            facultiesList.append(facultyObj) # Passing object
        except:
            print("Exception in faculty Object Creating")

        print(facultyObj.description()) #Old data


        enter = input("\n\n\t\t- Press any button to getback to the Main Menu")
        os.system('clear')    



    def updateFaculty ():
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Update Faculty Info\n\n")
        searchId = input("\n\n\n\t\tPlease Enter Faculty Id: ")
    
        for fac in facultiesList:
            
            if fac.id == searchId:
                print("\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n \n\n\t\tUpdate Data: ")
                fac.name  = input("\n\n\n\t\tPlease Enter new Faculty Name: ")

                print("\n\n\n\n\t\t\t Updated SUCSSESSFULLY \n\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n" )
                print(fac.description())
        
            else:  
                print("\n\n\n\n\t\t\t\tThis Faculty Id Doesn't Exist!!!! \n\n\n\n")

        enter = input("\n\n\t\t- Press any button to getback to the Main Menu")       
        os.system('clear') 
            

    def readFaculty ():
        found = False
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Read Faculty Info\n\n")
        searchId = input("\n\n\n\t\tPlease Enter Faculty Id: ")
        
        for fac in facultiesList:

            if fac.id == searchId:
                print(fac.description())
                found = True
                break
        
        if found == False:  
            print("\n\n\n\n\t\t\t\tThis Faculty Id Doesn't Exist!!!! \n\n\n\n")
        enter = input("\n\n\t\t- Press any button to getback to the Main Menu")       
        os.system('clear') 

    
    def description(self):
        return super().description() + "\n\n\t\t\tFaculty Departments: " +  str(self.departmentsSet) + " \n\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n"

    
    