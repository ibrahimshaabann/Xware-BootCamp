# import os
# departments = []

# class Department:
#     Id = None
#     name = None
    
#     def __init__(self, name, id) -> None:
#         self.id = id
#         self.name = name

#     def CreateDepartment (self):
#         print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Create Department \n\n")
#         department  = Department()
#         Id = input("\n\n\n\t\tPlease Enter Department Id: ")
#         name = input("\n\n\n\t\tPlease Enter Faculty Name: ")
#         departmentsInput = input("\n\n\n\t\tPlease Enter Space-Separated Departments: ")
#         departments = tuple(str(item) for item in departmentsInput.split())
    
#         print("\n\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n")
#         prof_list = linkProfsToFaculty()
#         faculties_list.append({'Id' : Id, 'name' : name, 'departments': departments, 'Professors': prof_list})
#         print(f"\n\n\t\tNew Data: \n\n\n\t\t\tFaculty Id: {Id} \n\n\t\t \tFaculty Name: {name} \n\n\t\t\tFaculty Departments: {departments} \n\n\n")
#         print("\n\n\n\t\t\t\t-------------------------------------------------------------------------- \n\n")
#         print(f"\n\n\t\tProfessor Id \t\t\t\tPrfoessor Name: \t\t\t\tProfessor Department \n\n")

#     for prof in prof_list :
#         print(f"\t\t{prof['profId']} \t\t\t\t\t\t {prof['profName']} \t\t\t\t\t\t {prof['profDep']} \n\n")

#     enter = input("\n\n\t\t- Press any button to getback to the Main Menu")
#     os.system('clear')    



# dep1 = Department("IS",11)