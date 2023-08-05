class BaseModel:
    id = None
    name = 8

    def __init__(self, id = None, name = None) :
        
        self.id = id
        self.name = name

    
    def description(self):
        print("\n\n\t\tHello from Base Model!!!!!!!")
        return  "\n\n\t\tData: \n\n\n\t\t\tFaculty Id: " + self.id + "\n\n\t\t \tFaculty Name: " + self.name 
    
