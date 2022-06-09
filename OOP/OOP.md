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

### Inheritance
* Inheritance is the capability of one class to derive or inherit the properties from another class.
* Child class can access the attributes of parent class, but parent class cannot access the attributes of child class.
* The type of the reference variable determines what attributes can be access.
* super().__ init__() is used to call parent constructor.

### Polymorphism
* Polymorphism means to be in multiple forms or multiple ways to represent.
* Polymorphism can be Compile-time polymorphism or Runtime polymorphism.
* Compile time polymorphism or Static polymorphism is achieved via method overloading.
* Method Overloading means a method is having same name but different type, ordering of type, argument or return type. Eg: Multiple Constructors.
* Python does not support Method Overloading.
* Runtime polymorphism or dynamic polymorphism is achieved by method overriding.
* Method Overriding means that the child class has the exact same method as the parent class, depending on object type.

### Encapsulation (yet to be implemented)
* Encapsulation is the idea of wrapping data and the methods that work on data within one unit (class).

### Abstraction (yet to be implemented)
* Abstraction is the property by virtue of which only the essential details are displayed to the user and hiding the unnecessary details.
