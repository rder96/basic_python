# Useful Built-in Functions/ Tips
1. zip() - map similar indeox of multiple containers -> to a single entity
   - param: python iterables or containers (list, string, etc) 
   - return: single **iterator** of **tuples** -> iterators can only be exhausted(by something like making a list out of them) once
     - purpose: save memory by only generating the elements of the iterator as you need them, vs putting all in memory at once
   - x = [1, 2, 3]
     y = [4, 5, 6]
     zipped = zip(x, y)
     list(zipped) -> [(1, 4), (2, 5), (3, 6)]
   - to **unzip**
     list(zip(*zipped)) -> [(1, 2, 3), (2, 4, 9)]
     by using *zipped, apply all tupples in zipped as separate arguments to the zip() function

2. Conventional use of _: 
   - To hold the result of the last executed expression(/statement) in an interactive interpreter session
   - As a general purpose "throwaway" variable name to indicate that part of a function result is being deliberately ignored (Conceptually, it is being discarded.),
     as in code like: label, has_label, _ = text.partition(':').
   - As part of a function definition (using either def or lambda), where the signature is fixed (e.g. by a callback or parent class API),
     but this particular function implementation doesn't need all of the parameters, as in code like: ```callback = lambda _: True```
   - The python linter recognizes the underscore as a purposefully unused variable (both use cases above). For example ```year,month,day = date()``` will raise a lint warning if the day variable is not used later on in the code,
     the fix if the day is truly not needed is to write ```year,month,_ = date()```. Same with lambda functions, ```lambda arg: 1.0``` is creating a function requiring one argument but not using it, that will be caught by lint, the fix is to write ```lambda _: 1.0```.
     An unused variable is often hiding a bug/typo (set day but used dya the next line).
   - For translation lookup in i18n (see the gettext documentation for example), as in code like ```raise forms.ValidationError(_("Please enter a correct username"))```.

# Tuples 
1. Tuple - ordered collection of values that cannot be modified at runtime.
   - similar to list (can be indexed/sliced/iterated over) 
   - but, contents cannot be changed. As an alternative, can create new tuples from existing tples
     - bigger_immutable = immutable + (5, 6)
     - smaller_immutable = immutable[0:2]
   - use tuples when number of items is consistent. E.g., useful for 2D game with X and Y coordinates.
     using a tuple with 2 numbers ensure that number of coordinates doesn't change
     - pos_x, pos_y = (0, 0)
       
# Sets
1. Sets - unordered collection of unique values that can be modified at runtime
   - simple_set = {0, 1, 2}
   - simple_set.add(3), simple_set.remove(0)
   - **unordered** as it does not allow **duplicate**
   - to define new set collection: 
     - new_set = set()
   - can do things like: 
     - finding intersect: common = new_set.intersection(else_set)
     - compute exclusive set: two_exclusive = two.difference(four) -> only in two but not in four
     - compute union: all = two.union(four)
     - check set A subset of B: assert a.issubset(b)
     - check set A superset of iteself: assert a.issuperset(a); a.issuperset(b)

# Dictionaries
1. From 3.7, dictionary entries are sorted in the order that they are defined or inserted
   - can update value for specific key: student_gpa["john"] = 10;
   - can update values for multiple keys: student_gpa.update(bob=10, mary=1000)
   - to access both key and value simultaneosly: this_dict.items()
     ```
     gpa_binary = []
     for student, gpa in student_gpa.items():
         assert student_gpa[student] == gpa
         gpa_binary.append(gpa)
   - to remove item from dict: pop()

# Comprehensions 
1. - want to create zeros -> so expression set to '0' since no computing is required
     - assert [0 for _ in range(5)] == [0] * 5 == [0, 0, 0, 0, 0]
   - tuple comprehension -> can find length for each word 
     ```
     words = ["cat", "mice"]
     tuple_comp = tuple(len(word) for word in words)
     assert tuple_comp == (3, 4)
   - set comprehension -> can find **unique** for each word
     ```
     set_comp = {len(word) for word in words}
     assert set_comp == {3, 4, 5}
     ```
   - dictionary comprehension -> can map each word to ites length 
     ```
     dict_comp = {word: len(word) for word in words}
     assert dict_comp = {"cat": 3, "mice": 4}

# Deque (double-ended queue) -> doubly linked list 
1. - support thread-safe, memory efficient **apend** and **pops** from either side of the deque with appox. O(1) in either direction
   - through list objects support similar operations, they are optimized for fast fixed-length operations, incur O(n) memeory movement costs for pop(0) and insert(0, v) operation which change both the size and position of the underlying data representation
   - ```
     from collections import deque
     dq = deque()
     dq.append(1) -> add new node to the right of the ll
     dq.appendleft(2) -> add new node to the left of the ll
     ```
   - deque can be iterated over to build any data structure
     ```
     assert [el for el in dq] == [1, 2, 3]
     assert tuple(el for el in dq) == (1, 2, 3)
     assert {el for el in dq} == {1, 2, 3}
     ```
   - deque can be used as a stack (LIFO)
     - dq.pop()
   - deque can be used as a queue (FIFO)
     - dq.popleft()
     
# Strings
1. - split() -> split_content = new_content.split(" | ") -> return list of strings
   - ```
     assert isinstance(split_content, list)
     assert len(split_content) == 2
     assert all(isinstance(item, str) for item in split_content)
     ```
     all() -> requires that all values are true
  - assert new_content.startswith(upper)\
    assert new_content.endswith(lower)
  - DELIMITER.join()
    
   
     
   
   
