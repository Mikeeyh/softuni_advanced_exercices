"""we can import a module using as:"""

import math
print(math.sqrt(5))

import math as mt
print(mt.sqrt(5))


"""
pip install -r requirements.txt 
Use it to install all modules needed automatically
"""

# -------------------------------------------------------------------------

import pandas as pd
print(pd.DataFrame({
    'Monday': ['Morning', 'Afternoon', 'Evening'],
    'Tuesday': ['Morning', 'Afternoon', 'Evening'],
    'Wednesday': ['Morning', 'Afternoon', 'Evening'],
    'Thursday': ['Morning', 'Afternoon', 'Evening'],
    'Friday': ['Morning', 'Afternoon', 'Evening'],
    'Saturday': ['Morning', 'Afternoon', 'Evening'],
    'Sunday': ['Morning', 'Afternoon', 'Evening']
}))

"""
      Monday    Tuesday  Wednesday   Thursday     Friday   Saturday     Sunday
0    Morning    Morning    Morning    Morning    Morning    Morning    Morning
1  Afternoon  Afternoon  Afternoon  Afternoon  Afternoon  Afternoon  Afternoon
2    Evening    Evening    Evening    Evening    Evening    Evening    Evening
"""

# -------------------------------------------------------------------------
import sys
from termcolor import colored, cprint

text = colored("Hello, world", "red", attrs=['bold', 'underline'])
print(text)
cprint("Hello, world", "green", "on red")
