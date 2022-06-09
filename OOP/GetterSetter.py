class Employee:
    __name="Default Name"                               # private member

    def set_name(self, name):                           # getter method
        assert len(name)>8,f" {name} is too short"
        self.__name=name

    def get_name(self):                                 # setter method
        return self.__name


sp=Employee()
print(sp.get_name())
sp.set_name("Sandip Palit")
print(sp.get_name())