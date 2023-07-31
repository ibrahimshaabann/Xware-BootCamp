import os 
import Faculty

os.system('clear') 

while True:

    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Welcome To College Management System \n\n\n\n")

    print("\n\t\t * Choose of the following: \n\n\n")

    print("\n\t\t\t 1- Faculty: \n\n")
    print("\n\t\t\t 2- Professors: \n\n")
    print("\n\t\t\t 3- Students: \n\n") 
    print("\n\t\t\t 4- Departments: \n\n")
    print("\n\t\t\t 5- Subjects: \n\n")
    print("\n\t\t\t 6- Courses: \n\n")
    print("\n\t\t\t 7- Exams: \n\n")
    print("\n\t\t\t 8- Exit: \n\n")
    entetiesOption = input("\n\t\t\t\t ->> Write Your option: ")

    if entetiesOption == '1' :
        os.system('clear')    
        Faculty.facultyMenu()

    elif entetiesOption == '2':
        pass

    elif entetiesOption == '3':
        pass

    elif entetiesOption == '4':
        pass

    elif entetiesOption == '5':
        pass

    elif entetiesOption == '6':
        pass

    elif entetiesOption == '7':
        pass

    elif entetiesOption == '8':
        print("\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t Thanks for using our System \n\n\n\n")
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t IBRAHIM SHAABAN \n\n\n\n")
        break

    else :
        print("\n\n\n\n\t\t\t\tWRONG OPTION!!!! \tplease enter a number from 1 to 7\n\n\n\n")




