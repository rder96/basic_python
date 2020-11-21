# Some notes about styling from python.org
1. Max line length
   - Limit all lines to max of 79 chars
   - For flowing long blocks of text (docstrings/comments) - line length should be limited to 72 chars

2. Preferred way of wrapping long lines - use Python's implied line continuation inside parantheses, brackets, braces.
Long lines can be broken over multiple lines by wrapping expressions in parentheses -> should be used in preference to backslash for line continuation.
   - but, long multiple **with-statements** cannot use implicit continuation
     ```
     with open('/path/to/some/file/you/want/to/read') as file_1, \
          open('/path/to/some/file/being/written', 'w') as file_2:
         file_2.write(file_1.read())
     ```
   - same with **assert** statements

3. Imports
   - NOTE: Imports should usually be on separate lines
     ```
     -> correct
     import os 
     import sys
     -> wrong
     import sys, os
   - It's ok to do:
     ```
     -> correct
     from subprocess import Popen, PIPE
     ```
   - Should be grouped in this order:
     1. Standard library imports
     2. Related third party imports
     3. Local app/library specific imports\
     Put a blank line between each group of imports
   - wildcard imports (from <module> import *) should be avoided -> unclear which names are present in the namespace
     (except to republish an internal interface as part of a public API)

4. Module Level Dunder Names - after module docstring but before any import statements except from __future__ (future-imports must appear in module before any other code except docstrings)

5. Whitespaces (important)
   - no whitespace:
     - immediately inside parentheses, brackets or braces -> spam(ham[1], {eggs: 2})
     - between a trailing comma and a following close paren -> foo = (0,)
     - immediately before comma, semicolon or colon -> if x ==4: print x, y; z
     - HOWEVER, in a slice, colon acts like a binary operator -> should have equal amounts on either side (treating it as the operator with lowest priority) 
       - in extended slice, both colons must have smae amount of spacing applied
       - exception: when slice parameter is omitted, space is omitted
       - ham[1:9], ham[lower+offset : upper+offset], ham[lower + offset : upper + offset]
     - **whitespace** added around operators with the **lowest priority**
     
6. Underscores in Numeric Literals (https://www.python.org/dev/peps/pep-0515/)
   - underscores can be used as visual separators for digit grouping purposes in integral, floating-point and complex number literals
   - no semantic meaning, parsed as if underscores were absent.
   
7. To access docstring of a method, use \__doc__ attribute. Remember, everything in Python is an object
