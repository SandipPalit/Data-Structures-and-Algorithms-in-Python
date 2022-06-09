class Employee:
    def display(self,name):
        print (name+" is in Employee class")


class IT_Employee(Employee):
    def display(self,name):                          # method overriding
        print (name+" is in IT_Employee class")


sp=IT_Employee()
sp.display("Sandip Palit")
