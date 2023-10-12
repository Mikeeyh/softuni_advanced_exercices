from math import sqrt
from modules.my_python_package.first import sqrt

print(sqrt(5))  # My func

"""
it returns the result from the second import (the last one which has been seen by python).
modules.my_python_package.first - We give the path to the function using '.'
"""

# How to use the two functions --------------------------------------

from math import sqrt
from modules.my_python_package.first import sqrt as my_sqrt

print(sqrt(5)) # 2.23606797749979
