from __future__ import division
import numpy as np
from math import *

# First, let's have us a dictionary of objects and their masses in kilograms
mass = [ ('a bag of sugar', 'bags of sugar',  1),
         ('an average man (UK)', 'average men (UK)', 70)
       ]
mass = np.array(mass, dtype=[('singular', '|S25'), 
                             ('plural', '|S25'),
                             ('mass', 'f')])

def find_nearest(array,value):
    """
    Finds the nearest item in the array to the inputted value
    """
    idx = (np.abs(array-value)).argmin()
    return idx

number  = raw_input('Please enter a mass (kg): ')
number  = float(number)
nearest = find_nearest(mass['mass'], number)



print 'In the region of', round(number / mass['mass'][nearest]), mass['plural'][nearest]
