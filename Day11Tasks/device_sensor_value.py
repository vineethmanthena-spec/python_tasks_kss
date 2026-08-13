#. Device Sensor Value (Scalar Array) 
#An IoT device records a single sensor reading = 75. Task: 
#● Create a 0-D NumPy array with this value. 
#● Print the value and check its number of dimensions.
import numpy as np
sensor_reading = np.array(75)

print("Sensor Value:", sensor_reading)

print("Number of Dimensions (ndim):", sensor_reading.ndim)
