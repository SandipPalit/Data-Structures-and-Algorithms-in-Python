class Employee:                                     # Parent class
    def __init__(self,name:str="Default Name"):
        self.name=name

    def display(self):
        print ("I am "+self.name)


class IT_Employee(Employee):                        # Child Class inheriting from parent class
    def __init__(self,name:str,dept:str):
        super().__init__(name)                      # calling parent constructor
        self.dept=dept

    def details(self):
        print ("I am "+self.name+" and my Department is "+self.dept)


sp=IT_Employee("Sandip Palit","Development")
sp.display()                                        # It will find display() in child class, if not found then it will search in parent class.
sp.details()