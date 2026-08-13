#. Splitting Student Scores Across Servers 
#A dataset: 
#[50, 60, 70, 80, 90, 100, 110, 120] 
#Scenario: 
#A distributed system needs to divide this data among 4 servers. 
#Task: 
#● Convert to NumPy array. 
#● Split the array into 4 equal parts using array_split(). 


import numpy as np

scores_list = [50, 60, 70, 80, 90, 100, 110, 120]

scores_array = np.array(scores_list)
print("Original Array:", scores_array)

server_splits = np.array_split(scores_array, 4)

for i, server_data in enumerate(server_splits, start=1):
    print(f"Server {i}: {server_data}")
