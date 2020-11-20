# Control FLow
1. For loops iterate over lists: 
   - for animal in ["dog", "cat", "mouse"]:
      print("{} is a mammal".format(animal))
   > NOTE: can use format()) to interpolate formatted strings
2. range(number) returns an **iterable** of numbers from zero to given no.
   - range(4): 0, 1, 2, 3
   - range(4, 8): 4, 5, 6, 7
   - range(4, 8, 2): range(lower, upper, step)
   - ```
     for i in range(4):
         print(i)
     ```
3. To loop over a list, and retrieve both invdex and value of each item in the list: 
- ```
  animals = ["dog", "cat", "mouse"]
  for i, value in enumerate(animals):
     print(i, value)
  ```
   - prints:\
     0 dog\
     1 cat\
     2 mouse
4. Handle exceptions with a try/except block
- ```
  try:
      -> NOTE: use "raise" to raise an error
      raise IndexError("This is an index error")
  except IndexError as e: 
      pass -> Pass is just a no-op
  -> Usually would do recovery here
  except (TypeError, NameError): 
      ...
  else:
      print("All good!)
  -> will execute under all circumstances
  finally:
      print("Clean resources")
  ```
5. Instead of doing try/finally to cleanup resources, can use a **with** statement
   - w+ -> open file for write + read, overwrite if file exists\
     r+ -> open file for write + read
   - ```
     with open("myfile.txt") as f:
         for line in f:
             print(line)
     ```
   - Write to a file:
     ```
     with open("myfile.txt, "w+") as file: 
         file.write(str(contents)) -> write a string to a file
     ```
     ```
     with open("myfile2.txt, "w+") as file:
         file.write(json.dumps(contents)) -> write an object to a file
     ```
   - Read from a file:
     ```
     with open("myfile.txt, "r+") as file:
         contents = file.read() -> reads a string from a file
         contents = json.load(file) -> reads a json object from a file

## Iterable and iterator
6. fundamental abstraction - **Iterable** - object that can be treated as a sequence.\
E.g. most built-in containers in Python like: list, tuple, string etc are iterables.\
E.g.2 The object returned by the range function, is an iterable.
- ```
  dict = {"one": 1, "two": 2}
  our_iterable = dict.keys()
  print(our_iterable) -> dict_keys(['one', 'two']) -> an object that implements our Iterable interface
  ```
  - we can loop over it
    ```
    for i in our_iterable: 
        print(i) -> prints one, two
  - However, cannot address elements by index! 
    - our_iterable[1] -> Raises a TypeError
7. **Iterator** - object that can remember the state as we traverse through it.\
(Iterable is an object that knows how to create an iterator)
   - use "next()" to get the next object
     ```
     our_iterator = iter(our_iterable)
     next(our_iterator) -> "one"
     ```
   - After iterator has returned all its data, raises a StopIteration exception
     next(our_iterator) -> Raises StopIteration
   - We can also loop over it (what "for" does implicitly)
     ```
     our_iterator = iter(our_iterable)
     for i in our_iterator:
         print(i) -> "one", "two"
     ```
   - Grab all elements of **iterable** or **iterator** by calling list()
     ```
     list(our_iterable) -> ["one", "two"]
     list(our_iterator) -> returns [] because state is saved! - we traversed it earlier
     ```

# Functions
8. Use "def" to create new functions.
- ```
  def add(x, y): 
      print("x is {} and y is {}".format(x, y))
      return x + y
  add(5, 6)
  add(y=6, x=5)
  ```
   - func can take a **variable number** of **positional arguments**
     ```
     def varargs(*args):
         return args
     varargs(1, 2, 3) -> (1, 2, 3)
     ```
   - func can take a **variable number** of **keyword args**
     ```
     def keyword_args(**kwargs):
         return kwards
     keyword_args(big="foot", loch="ness") -> {"big": "foot", "loch": "ness"}
     ```
   - can do both at once
     ```
     def all_args(*args, **kwargs):
         print(args) -> (1, 2)
         print(kwargs) -> {"a": 3, "b": 4} 
     all_args(1, 2, a=3, b=4)
     ```
   - when calling functions, can do opposite of args/kwargs\
     use * to expand tuples and ** to expand kwargs
     ```
     args = (1, 2, 3, 4)
     kwargs = {"a": 3, "b": 4}
     all_args(*args) -> same as all_args(1, 2, 3, 4)
     all_args(**kwargs) -> same as all_args(a=3, b=4)
     ```

9. function scope
   - x = 5 in function - local
   - global x = 6 in function - global
   - x in 10 outside function - global
 
 10. - Python has **first-class** function - treats functions as first-class citizens (support passing functions as args to other funcs, returning them as vals from other funcs and assigning them to vars or storing them in data structs
     - also has **anonymous(lambda) functions** (save time + effort + memory)
       - keyword used: lambda, can have only 1 expression
       - Syntax: lamda parameter : action(parameter)
       - (lambda x: x > 2)(3) -> True
       - (lambda x, y: x ** 2 + y ** 2)(2, 1) -> 5
     - there are **built-in higher order functions**
       - list(map(add_10, [1, 2, 3])) -> [11, 12, 13]
       - list(map(max, [1, 2, 3], [4, 2, 1])) -> [4, 2, 3]
       - list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])) -> [6, 7]
     - can use **list comprehensions** for nice **maps and filters**\
       list comprehensions - store output as a list which can itself be a nested list
       - [add_10(i) for i in [1, 2, 3]] -> same as above
       - [x for x in [3, 4, 5, 6, 7] of x > 5] -> same
     - can construct **set** and **dict comprehensions** as well
       - {x for x in 'abcdddeeeff' if x not in 'abc'} -> {'d', 'e', 'f'}
       - {x: x**2 for x in range(5)} -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
       
       
             
     
  
  
    
