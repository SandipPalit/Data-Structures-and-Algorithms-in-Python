##Observations

* By default, python uses 'Call by Reference'. For 'Call by Value', we need to use deepcopy().
* In “deepcopy()” function,  any changes made to a copy of object do not reflect in the original object. In “copy()” function, any changes made to a copy of object do reflect in the original object.

### Access Modifiers
* Public means we can access it from anywhere
* Protected means we can access from that class or it's sub-classes. We make a variable protected by adding "_" as prefix.
* Private means we can access only from that class itself. We make a variable private by adding "__" as prefix.
* Python achieves this by Name Mangling, i.e,  any identifier with two leading underscore and one trailing underscore is textually replaced with _classname__identifier where classname is the name of the current class.

### Class & Object
* A class is a template for an object, and an object is an instance of a class.
* Object is the real-world entity.
* An Object consist of state (attributes), behavior (methods) and identity (unique name).
* Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute
* self keyword will always point to the Current Object.
* Different classes can be kept within a package(folder) and can be accessed using the import keyword.

### Constructor & Destructor:
* Python does not support explicit multiple constructors.
* __ init__ and __ del__ are magic functions also known as constructors and destructors resp.
* assert keyword is used to continue the execution if the given condition evaluates to True.

### Exception Handling
* raise keyword allows us to throw an exception manually.
* In the try block, all statements are executed until an exception occurs.
* except keyword is used to catch and handle the exceptions.
* else block is executed only when no exception occurred in the try block.
* finally block executes irrespective of exception.

### Getters and Setters
* Getters and Setters are used in Data Hiding to hide the private members from direct access.
* We also use getters & setters to add validation logic around getting and setting a value.
