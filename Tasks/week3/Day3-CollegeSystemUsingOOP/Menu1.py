import os
from Faculty1 import Faculty
from Department1 import Department
from Professor1 import Professor

class FacultyMenu:

    def facultyMenu():
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Faculty \n\n")
        print("\n\t\t * Choose of the following: \n\n\n")
        print("\n\t\t\t 1- Create Faculty: \n\n")
        print("\n\t\t\t 2- Read Faculty Info: \n\n")
        print("\n\t\t\t 3- Update Faculty Info: \n\n") 
        facultyOption = input("\n\t\t\t\t ->> Write Your option: ")
   
        if facultyOption == '1' :
            os.system('clear') 
            Faculty.createFaculty()
               

        elif facultyOption == '2':
            os.system('clear')    
            Faculty.readFaculty()

        elif facultyOption == '3':
            os.system('clear')
            Faculty.updateFaculty()

        elif facultyOption == '4':
            pass

        elif facultyOption == '5':
            pass    


    def departmentMenu():
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Department \n\n")
        print("\n\t\t * Choose of the following: \n\n\n")
        print("\n\t\t\t 1- Add Department: \n\n")
        print("\n\t\t\t 2- Delete Department: \n\n")
        print("\n\t\t\t 3- Update Faculty Info: \n\n") 
        depOption = input("\n\t\t\t\t ->> Write Your option: ")
   
        if depOption == '1' :
            os.system('clear') 
            Department.addDepartments()
               

        elif depOption == '2':
            os.system('clear')    
            Faculty.readFaculty()

        elif depOption == '3':
            os.system('clear')
            Faculty.updateFaculty()

        elif depOption == '4':
            pass

        elif depOption == '5':
            pass


    def professorMenu():
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Professor \n\n")
        print("\n\t\t * Choose of the following: \n\n\n")
        print("\n\t\t\t 1- Add Professor: \n\n")
        print("\n\t\t\t 2- Show Professors: \n\n")
        print("\n\t\t\t 3- Update Faculty Info: \n\n") 
        depOption = input("\n\t\t\t\t ->> Write Your option: ")
    
        if depOption == '1' :
            os.system('clear') 
            print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Add Professor \n\n")
            FacId = input("\n\n\n\t\tPlease Enter Faculty Id you want to add professors into: ")
            profId = input("\n\n\n\t\tPlease Enter professor Id: ")
            profFirstName = input("\n\n\n\t\tPlease Enter professor First Name: ")
            profLastName = input("\n\n\n\t\tPlease Enter professor Last Name: ")

            profAge = int(input("\n\n\n\t\tPlease Enter professor Age: "))
            profDepartment = input("\n\n\n\t\tPlease Enter professor department: ")

            profObject = Professor(profId, profFirstName, profLastName,  profAge, profDepartment)
            Professor.addProfessor(profObject, FacId)
            enter = input("\n\n\t\t- Press any button to getback to the Main Menu")       

            os.system("clear")
                

        elif depOption == '2':
            os.system('clear')  
            FacId = input("\n\n\n\t\tPlease Enter Faculty Id you want to add professors into: ") 
            print(f"\n\n-------------------------------------------------------------------------------------------------\n\n\n\n\t\tProfessors") 
            Professor.showProfessors(FacId)
            enter = input("\n\n\n\n\t\t- Press enter to getback to the Main Menu")       
            os.system("clear")

        elif depOption == '3':
            os.system('clear')
            Faculty.updateFaculty()

          
