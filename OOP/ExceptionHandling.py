class Employee:
    def divide(self, a, b):
        try:                                                    # try block
            if a<b:
                raise Exception(f'{a} is lesser than {b}')
            print("Answer is ",a/b)
        except Exception as ex:                                 # except block
            print("Exception:  ",ex)
            print("Within Except block")
        else:                                                   # else block
            print("Within Else block")
        finally:                                                # finally block
            print("Within Finally block")


sp=Employee()
sp.divide(21,0)