# Random basic knowledge about python (learnxinyminutes)
# types
1. 7%3 = 1 but -7%3 = 2
   > i % j have the same sign as j, unlike C
   > http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
2. for string literals, can do both: "hello" + "world" and "hello" "world"
    - "hello world"[0] = h
    - f-strings/ formatted strings: f"She said her name is {name}"
    - f"{name} is {len(name)} long" - You can basically put any Python expression inside the braces and it will be output in the string.
3. 0 and 2 -> 0; -5 or 0 -> -5 
   - None, 0, and empty strings/lists/dicts/tuples all evaluate to False.
   - All other values are True
4. None is an object
   - Don't use the equality "==" symbol to compare objects to None. Use "is" instead. This checks for equality of object identity.
     - "etc" is None  # -> False
     - None is None   # -> True
- True and False
- no && ||, but binary AND (&) and binary OR (|)
# functions
5. By default the print function also prints out a newline at the end. Use the optional argument end to change the end string.
   - print("Hello, World", end="!")  # -> Hello, World!
6. Simple way to get input data from console
   - input_string_var = input("Enter some data: ") # Returns the data as a string
7. if can be used as an expression
   - "yay!" if 0 > 1 else "nay!"  # -> "nay!"
# list
8. list=[1, 2, [3, 4, 5]] vs array -> need to import array module
   - import array
   - array is a vector storing data of the same data type, else will output exception
   - more compact in memory (since elements allocated with contiguous memory location)
9. list operations
   - li.append() -> add to the end 
   - li.pop() -> remove from end
   - slicing -> closed/open range, i.e. inclusive/exclusive
     - li[2:4]
     - li[start: end:step]
   - one layer deep copy (li2 is li = false)
     - li2 = li[:]
   - remove arbituary element from list with del 
     - del li[1]
   - remove first occurence of arg
     - li.remove(2) -> will remove the first 2 found
   - insert at specific index
     - li.insert(1, 2)
   - find index of arg
     - li.index(4)
   - adding list (original lists are not modified) 
     - li + li2 = [1, 2, 3, 4, 5, 6]
   - concat list with extend(), li concatenated, li2 no change (obvious)
     - li.extend(li2) -> li = [1, 2, 3, 4, 5, 6]
  # tuples
  - tuples are like list but immutable
  - can do most operations of list with tuple
  10. tup = (1, 2, 3) 
      - tup[1] -> 2
      - tup[2] = 3 -> error
      - NOTE: tuple of length 1 must have comma after the last element but not for other lengths(even zero) 
        - type((1)) -> integer
        - type((1, )) -> tuple
        - type(()) -> tuple
	    - unpack tuple into variables
        - a, b, c = (1, 2, 3) || a, b, c = 1, 2, 3
      - extended unpacking 
        - a, *b, c = (1, 2, 3, 4) -> b = [2, 3] => b is a list! 
        - * is an list empty by default
      - swapping: 
        - e, d = d, e
# dictionaries
11. dict = {"one": 1, "two": 2, "three": 3}
- NOTE: keys have to be immutable type(ints, floats, tuples, strings) but values can be of any types
  - invalid_dict = {[1,2,3]: "123"}
  - valid_dict = {(1,2,3):[1,2,3]}
- to look up values in dict -> []
  dict["one"] = 1
  dict[(1, 2, 3)] = [1, 2, 3]
- list(dict.keys()) -> create a list with keys
  - for python 3.7>=, keys and values are ordered the way they are inserted
- list(dict.values())
- check existence of keys using "in" 
  - "1" in list -> True
- dict["four"] returns error, use get() to avoid KeyError
  - dict.get("1") -> 1
  - dict.get("4") -> None
  - NOTE: get value also support default value if result missing! 
    - dict.get("1", 4) -> 1
    - dict.get("4", 4) -> 4 (default)
- "setdefault()" inserts into a dictionary only if the given key isn't present
  - dict.setdefault("5", 5) - "5": 5
  - dict.setdefault("5", 6) - "5" no change since 5 is present!
- delete from dict: 
  - del dict["one"]
- additional unpacking options: 
  - {'a': 1, **{'b': 2}} -> {'a': 1, 'b': 2}
  - ** latter will always overwrite previous: 
    - {'a': 2, **{'a': 3} -> {'a': 3}
  -https://www.python.org/dev/peps/pep-0448/
# sets
sets store sets (mathematical) -> no duplicated elements, unordered, set looks like dict! 
- https://stackoverflow.com/questions/30571285/how-to-check-if-a-value-is-present-in-any-of-given-sets/30571351#30571351 - it is best to create set this way
- set = {1, 2, 2, 3, 3, 3, 4} -> set = {1, 2, 3, 4}
- similar to dict's elements, set stores immutable elements
  - set = {[1, 2], 3} -> TypeError
  - set = {(1, ), 3} -> OK
- add item to set
  - set.add(-1)
- set intersection - &
  - other_set = {2, 3, 5} 
  - set & other_set = {2, 3} (return a set)
- set union - | 
  - set | other_set = {1, 2, 3, 4, 5} 
- set difference - - (set with elements in 1st not in 2nd) 
  - set - other_set = {1, 4}
- set symmetric difference - ^
  - set ^ other_set = {1, 4, 5} 
- check left superset right -> left >= right -> Bool
- check left subset right -> left <= right -> Bool
- check existence using in
- one deep layer copy: filled_set = set.copy() 
  - filled_set is set -> False
