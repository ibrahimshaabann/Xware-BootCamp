class Student:
    id = None #None indicates the initial value of the attribute
    name = None
    age = None

    def __init__(self, id, name, age) :
          self.id = id
          self.age = age
          self.name = name

    


class Professor:
    id = None
    name = None
    phone = None


class StudentEnrollment:
    id = None #None indicates the initial value of the attribute
    student = None
    subject = None

    def enrolStudent(self, student, subject): #self is like this in java but you must write it (it is not optional)
        self.student = student
        self.subject = subject
    
    def __init__(self, id = None, student = None, subject = None) :  # You are allowed to create on constructor only in python
        print(id)
        


# This an object of student 
student1 = Student(1, "Tarek", 12) #shortcut ctrl + d Select 
# student1.id = 1
# student1.name = "Ibrahim"
# student1.age = 21
print(student1.name)
print(student1.age)
print("______________________________")




# We will enroll student 1 in a course
stu_enr = StudentEnrollment() #In this case we didn't pass values to the constructor so the defauly value is passed
stu_enr.student = student1 # Refernce to  the created student1 object
stu_enr.id = 1


print("-->>>>>>>>>>>This is the address of the object", stu_enr)
print(stu_enr.student)

