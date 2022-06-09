class Employee:
    name="Sandip Palit"                 # public
    _id=9                               # protected
    __dept="IT"                         # private


sp=Employee()
print(sp.name)                          # we can directly access public member
print(sp._id)                           # we can directly access protected member
# print(sp.__dept)                      # we cannot directly access private member
print(sp._Employee__dept)               # we can only access private member using name wangling
