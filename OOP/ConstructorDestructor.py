class Employee:
    def __init__(self,name:str="Default Name"):     # __init__      -->     constructor     (str --> data type  &  "Default Name" --> default value)
        assert len(name)>8,f" {name} is too short"  # validation
        self.name=name

    def display(self):
        print ("I am "+self.name)

    def __del__(self):                              # __del__       -->     destructor
        print("Object ("+self.name+") destroyed")


sp=Employee()
sp.display()
sp=Employee("Sandip Palit")
sp.display()