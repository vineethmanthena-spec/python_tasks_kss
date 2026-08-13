#Q: Bank Transaction Storage 
#A bank stores the transaction amounts of a customer in a list: 
#[1200, 500, 800, 1500] Scenario: 
#● Convert the list into a NumPy array. 
#● Print the type of the object. 
#● Verify that it is a NumPy ndarray

import numpy as np

transactions_list = [1200, 500, 800, 1500]

transactions_array = np.array(transactions_list)

print("Type:", type(transactions_array))

print("Is ndarray:", isinstance(transactions_array, np.ndarray))