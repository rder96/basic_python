# Modules
1. - import modules
     ```
     import math
     print(math.sqrt(16)) -> need to call from math
   - to get specific functions from a module
     ```
     from math import ceil, fllor
     print(ceil(3.7)) 
     print(floor(3.7))
     ```
   - can import all functions from a module (not recommended)\
     ```from math import *```
   - shorten module names
     ```
     import math as m
     math.sqrt(16) == m.sqrt(16) -> True
     ```
2. Python modules are just ordinary Python files. Can write your own and import them.
   - Name of module is name of file
   - To find out which functions and attributes are defined in a module:
     > - everything in python is an object -> almost everything has attributes and methods\
     > - attribute=properties - characteristic of an object, can be divided into states (defined using variables)/behaviors(implemented using methods)\
     > - functions can be an attributes of a class, or called methods\
     > - all functions have built-in attribute \__doc__ -> returns doc string defined in function source code
     - dir(math)
   - NOTE: If have a Python script named math.py in the same folder as current script, math.py will be loaded instead of built-in Python module.
     - Local folder has priority over Python's built-in libraries

# Classes
3. ```
   class Human:
       species = "H. sapiens" -> A class attribute, it is shared by all instance of this class
       
       -> Basic initializer, called when this class is instantiated
       -> double leading+trailing underscores - objects/attributes that are used by Python but live in user-controlled nameespaces
       -> Methods/objects/attributes like __init__, __str__, __erepr__ etc are called special methods
       -> SHOULD NOT invent such names on your own
       def __init__(self, name):
           self.name = name 
           self.age = 0 -> initialize property
       
       -> An instance method, all methods take "self" as first arg
       def say(self, msg): 
           print("{name}: {message}".format(name=self.name, message=mseg))
       
       def sing(self):
           return 'hello'
        
        -> A class method is shared among all instances
        -> called with the calling class(cls - like self above) as the first arg 
        @classmethod
        def get_species(cls):
            return cls.species
        
        -> A static method - called w/o a class/instance reference
        -> Generally, utility methods
        @static method
        def grunt():
            return "*grunt*"
        
        -> A property is just like a getter
        -> turns the method age() into an read-only attribute of the same time
        -> no need to write trivial getters and setters in Python
        @property
        def age(self):
            return self._age
        
        -> This allows property to be set
        @age.setter
        def age(self, age):
            self._age = age
        
        -> This allows property to be deleted
        @age.deleter
        def age(self):
            del self._age           
   ```
   - https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters

4. This \__name__ check makes sure this code block is only executed when this module is the main program.
   ```
   if __name__ == '__main__': 
       -> instantiate a class
       i = Human(name="Ian")
       i.say("hi")
       
       -> to call class method:
       i.say(i.get_species())
       -> to change shared attribute
       Human.species = "H. something"
       -> to call static method - call by class or instances
       print(Human.grunt())
       print(i.grunt())
       
       -> update property for this instance
       i.age = 42
       -> to get the property
       i.say(i.age)
       -> to delete the property
       del i.age
   ```

## Inheritance
5. Allow new child classes to be defined, inherit methods and vars from their parent class
   - To take advantage of modularization by file, place the classes above in their own files, e.g. human.py
   - To import functions from other files, use: from "filename-w/o-extension" import "function-or-class"
   ```
   -> Specify parent class(es) as parameters to the class definition
   class Superhero(Human):
       -> if child class should inherit all of the parent's definition w/o modifications, just use "pass" (nothing else)
       -> else, don't do pass and:
       species = 'Superhuman'
       -> Childrren automatically inherit their parent class's constructor including its arguments,
       -> but can also define additional args or defs and override its methods
       def __init__(self, name, movie=False, superpowers=["nothing"];
           -> add additional class attributes
           self.fictional = True
           self.movie = movie
           -> !! be aware of mutable(e.g. list) default values, since defaults are shared
           self.superpowers = superpowers
           -> To access parent class's methods that are overridden, use "super"
           super().__init__(name) ------> NOTE!!
       
       -> methods(override or additional)
       def sing(self):
           return 'Sing'
   
   if __name__ == '__main__':
       sup = Superhero(name="Tick")
       
       -> Instance type checks - since it inherits from Human but type is Superhero
       if isinstance(sup, Human): 
           do something
       if type(sup) is Superhero:
           do something
       
       -> Get the Method Resolution search Order used by both getattr() and super()
       -> This attribute is dynamic and can be updated (human here is the module/file name)
       print(Superhero.__mro__) -> (<class '__main__.Superhero'>, <class 'human.Human'>, <class 'object'>)
       
       -> can call all methods+attributes in both parent and own(including overridden methods)
       -> to call methods
       sup.say('Spoon')
       -> to use attribute (NOTE: no ())
       sup.age = 31 
       print(sup.movie)

## Multiple Inheritance
6. from superhero import Superhero\
from bat import Bat
   ```
   -> Define Batman, child that inherits from both Superhero amd Bat
   class Batman(Superhero, Bat): 
       
       -> use *args and **kwargs for clean way to pass args
       def __init__(self, *args, **kwargs):
       -> Typically to inherit attributes, have to call super: 
       -> super(Batman, self).__init__(*args, **kwargs)
       -> but super() only works with next base class in the MRO list.
       -> so explicitly call __init__ for all ancestors.
       Superhero.__init__(self, 'anonymous', movie=True,superpowers=['Wealthy'], *args, **kwargs)
       -> override ancestor's default attribute can_fly
       Bat.__init__(self, *args, can_fly=False, **kwargs)
       -> override value for the name attribute
       self.name = 'Sad Affleck'
       
   if __name__ == '__main__': 
       sup = Batman()
       
       -> Get Method Resolution search Order by both getattr() and super()
       print(Batman.__mro__) -> (<class '__main__.Batman'>, <class 'superhero.Superhero'>,
                             -> <class 'human.Human'>, <class 'bat.Bat'>, <class 'object'>)
       print('Can I fly? ' + str(sup.fly)) -> Can I fly? False
   ```

# Advanced
### Generators help you make lazy code.
```
def double_numbers(iterable):
    for i in iterable:
        yield i + i
```
7. Generators are **memory-efficient** because they only load the data needed to process the data 
needed to process the next value in the iterable.
   - can perform operations on otherwise prohibitively large value ranges
   ```
   -> range is a generator
   for i in double_numbers(range(1, 900000000)):
        print(i)
        if i >= 30:
        break
   ```
   - just like list comprehension, can also create generator comprehensions
   ```
   values = (-x for x in [1,2,3,4,5])
   for x in values:
       print(x) -> prints -1 -2 -3 -4 -5
   ```
   - can also cast a generator comprehension directly to a list
   ```
   gen_to_list = list(values)
   print(gen_to_list) -> [-1, -2, -3, -4, -5]
   ```
   
8. Decorators 
   - In this example, beg wraps say. If say_please is True then it will change the returned message.
   ```
   from functools import wraps
   
   def beg(target_function):
       @wraps(target_function)
       def wrapper(*args, **kwargs):
           msg, say_please = target_function(*args, **kwargs)
           if say_please:
               return "{} {}". format(msg, "Please! I am poor :(")
           return msg
       
       return wrapper
   
   @beg
   def say(say_please=False):
       msg = "Can you buy me a beer?"
       return msg, say_please
       
   print(say()) -> Can you buy me a beer?
   print(say(say_please=True)) -> Can you buy me a beer? Please! I am poor :(
   ```
      
  




























