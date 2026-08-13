# Copy vs View Behavior in Data Processing 
#Scenario: 
#A dataset: 
#[10, 20, 30, 40] 
#Task: 
#● Create a copy of the array. 
#● Modify the original array. 
#● Show that the copy does not change. 
#● Repeat using view() and observe the difference.

import numpy as np

original = np.array([10, 20, 30, 40])
arr_copy = original.copy()
original[0] = 99
original = np.array([10, 20, 30, 40])
arr_view = original.view()
original[0] = 99
