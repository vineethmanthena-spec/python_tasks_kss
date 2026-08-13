#. Filter High Temperature Values 
#A weather station records temperatures: 
#[28, 31, 35, 27, 40, 22] 
#Scenario: 
#The system needs temperatures above 30°C. 
#Task: 
#● Filter the values greater than 30 using NumPy boolean filtering.

import numpy as np
temperatures = np.array([28, 31, 35, 27, 40, 22])
mask = temperatures > 30

high_temps = temperatures[mask]
print(high_temps)

