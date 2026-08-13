#Product Rating System 
#An e-commerce website stores product ratings: 
#[4, 5, 3, 4, 2] 
#Task: 
#● Convert it to a NumPy array. 
#● Print the first and last rating using indexing.

import numpy as np

ratings = np.array([4, 5, 3, 4, 2])

print("First rating:", ratings[0])
print("Last rating:", ratings[-1])
