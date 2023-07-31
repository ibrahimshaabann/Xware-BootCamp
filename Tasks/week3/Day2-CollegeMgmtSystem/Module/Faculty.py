import os
faculties_list =[]

def facultyMenu():
    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Faculty \n\n")
    print("\n\t\t * Choose of the following: \n\n\n")

    print("\n\t\t\t 1- Create Faculty: \n\n")
    print("\n\t\t\t 2- Read Faculty Info: \n\n")
    print("\n\t\t\t 3- Update Faculty Info: \n\n") 
    facultyOption = input("\n\t\t\t\t ->> Write Your option: ")
   
    if facultyOption == '1' :
        os.system('clear')    
        createFaculty()

    elif facultyOption == '2':
        os.system('clear')    
        readFaculty()

    elif facultyOption == '3':
        os.system('clear')
        updateFaculty()

    elif facultyOption == '4':
        pass

    elif facultyOption == '5':
        pass


def createFaculty ():
    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Create Faculty \n\n")
    Id = input("\n\n\n\t\tPlease Enter Faculty Id: ")
    name = input("\n\n\n\t\tPlease Enter Faculty Name: ")
    departmentsInput = input("\n\n\n\t\tPlease Enter Space-Separated Departments: ")
    departments = tuple(str(item) for item in departmentsInput.split())
    
    print("\n\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n")
    prof_list = linkProfsToFaculty()
    faculties_list.append({'Id' : Id, 'name' : name, 'departments': departments, 'Professors': prof_list})
    print(f"\n\n\t\tNew Data: \n\n\n\t\t\tFaculty Id: {Id} \n\n\t\t \tFaculty Name: {name} \n\n\t\t\tFaculty Departments: {departments} \n\n\n")
    print("\n\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n")

    print(f"\n\n\t\tProfessor Id \t\t\t\tPrfoessor Name: \t\t\t\tProfessor Department \n\n")

    for prof in prof_list :
        print(f"\t\t{prof['profId']} \t\t\t\t\t\t {prof['profName']} \t\t\t\t\t\t {prof['profDep']} \n\n")

    enter = input("\n\n\t\t- Press any button to getback to the Main Menu")
    os.system('clear')    


def updateFaculty ():
    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Update Faculty Info\n\n")
    searchId = input("\n\n\n\t\tPlease Enter Faculty Id: ")
   
    for fac in faculties_list:
        
        if fac['Id'] == searchId:
            print(f"\n\n\t\tOld Data: \n\n\n\t\t\tFaculty Id: {searchId} \n\n\t\t \tFaculty Name: {fac['name']} \n\n\t\t\tFaculty Departments: {fac['departments']} \n\n\n")
            print("\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n")
            print("\n\n\t\tUpdate Data: ")
            name = input("\n\n\n\t\tPlease Enter new Faculty Name: ")
            departmentsInput = input("\n\n\n\t\tPlease Enter Space-Separated new Departments: ")
            departments = tuple(str(item) for item in departmentsInput.split())
            fac['name'] = name
            fac['departments'] = departments
            print("\n\n\n\n\t\t\t Updated SUCSSESSFULLY")
            print("\n\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n")
            print(f"\n\n\t\tNew Data: \n\n\n\t\t\tFaculty Id: {searchId} \n\n\t\t \tFaculty Name: {name} \n\n\t\t\tFaculty Departments: {departments} \n\n\n")
       
        else:
            print("\n\n\n\n\t\t\t\tThis Faculty Id Doesn't Exist!!!! \n\n\n\n")

    enter = input("\n\n\t\t- Press any button to getback to the Main Menu")       
    os.system('clear') 
        

    


def readFaculty ():
    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Read Faculty Info\n\n")
    searchId = input("\n\n\n\t\tPlease Enter Faculty Id: ")
    
    for fac in faculties_list:

        if fac['Id'] == searchId:
            print(f"\n\n\n\n\t\tData: \n\n\n\t\t\tFaculty Id: {searchId} \n\n\t\t \tFaculty Name: {fac['name']} \n\n\t\t\tFaculty Departments: {fac['departments']} \n\n\n")
            
        else:
            print("\n\n\n\n\t\t\t\tThis Faculty Id Doesn't Exist!!!! \n\n\n\n")

    enter = input("\n\n\t\t- Press any button to getback to the Main Menu")       
    os.system('clear') 



def linkProfsToFaculty():
    profs_list = []
    numOfProfsToEnter = int(input("\n\n\n\t\tPlease Enter How Many professors you want to enter: "))   
    for count in range(numOfProfsToEnter):
        print(f"\n\n\n\t\tProfessor {count + 1 }: ")
        profId = input("\n\n\n\t\tPlease Enter Professor Id: ")
        profName = input("\n\n\n\t\tPlease Enter Professor Name: ")
        profDep = input("\n\n\n\t\tPlease Enter Professor Department: ")
        profs_list.append({'profId': profId, 'profName':profName, 'profDep': profDep})
        print("\n\n\n\n\t\t\t ADDED SUCSSESSFULLY")
        enter = input("\n\n\t\t- Press any button to add the next Professor")    
    os.system("clear")   
    return  profs_list

        
 
    
    print("\n\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n")
