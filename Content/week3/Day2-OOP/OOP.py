# class Student:
#     id = None #None indicates the initial value of the attribute
#     name = None
#     age = None

#     def __init__(self, id = None, name = None, age = None) : # The two underscore before init idicates that it is a special method
#           self.id = id
#           self.age = age
#           self.name = name

    


# class Professor:
#     id = None
#     name = None
#     phone = None



#   # On the other hand, class attributes are attributes that have the same value for all class instances.
#   # You can define a class attribute by assigning a value to a variable name outside of .__init__().
#   # Class attributes must always be assigned an initial value
#   # Use class attributes to define properties that should have the same value for every class instance.
#   # Use instance attributes for properties that vary from one instance to another

# class StudentEnrollment:
#     department = "CS" #---------------> this is a class attribute

#     def enrolStudent(self, student, subject): #self is like this in java but you must write it (it is not optional)
#         pass
    

#     #self.name = name creates an attribute called name and assigns to it the value of the name parameter.
#     # Attributes created in .__init__() are called instance attributes. An instance attribute’s value is specific to a particular instance of the class.

#     def __init__(self, id = None, student = None, subject  = None) :  # You are allowed to create on constructor only in python
#         self.student = student
#         self.subject = subject
        


# # This an object of student 
# student1 = Student() #shortcut ctrl + d Select 
# # student1.id = 1
# # student1.name = "Ibrahim"
# # student1.age = 21
# student1.Ibrahim = "Hello, ibrahim"
# print(student1.name)
# print(student1.age)
# print(student1.Ibrahim) # This  is an attribute named Ibrahim specific to this object Only 

# print("______________________________")




# # We will enroll student 1 in a course
# stu_enr = StudentEnrollment() #In this case we didn't pass values to the constructor so the defauly value is passed
# stu_enr.student = student1 # Refernce to  the created student1 object
# stu_enr.id = 1


# print("-->>>>>>>>>>>This is the address of the object", stu_enr)
# print(stu_enr.student)




# #Difference between encapsulation and Information hiding
# # encapsulation describes bundling data and methods that work on that data within one unit, like a class in Java. 
# # We often often use this concept to hide an object’s internal representation or state from the outside. This is called information hiding.

# Parent Class
class Employee: 
    raise_amount = 0.2
    def __init__(self, fname = None, lname = None, pay = None):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        print(f"\n\tself: {self}")


    def applyRaise (self):
        pass

# Child Class
class Developer(Employee):
    raise_amount = 0.3 # This doesn't affect the parent class

    def __init__(self, fname = None, lname = None, pay = None, programmingLanguage = "None"): # This init is owned to child
        self.programmingLanguage = programmingLanguage
        super().__init__(fname , lname , pay ) 
        
    
    def description(self):
        print(f"\n\tEmployee Description: \n\n\tName : {self.fname + self.lname} \n\tPay: {self.pay} \n\tProgramming Language: {self.programmingLanguage}"   )




developer1 = Developer("Ibrahim", "Shaaban", 20, "Python")
developer1.description()

print(f"\n\tObject Location: {developer1}")
print(f"\n\tObject Location using id : {id(developer1)}")


print(isinstance(developer1, Employee))
print(isinstance(developer1, Developer))
print(Developer.mro()) # mro --------> method resolution Order ----> the logic order of how constructors excute



