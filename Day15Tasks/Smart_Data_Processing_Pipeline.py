#Smart Data Processing Pipeline 
#Scenario: 
#A system processes numeric data from file. 
#Task: 
#● Read numbers from a file 
#● Use NumPy for calculations (mean, std) 
#● Convert results to Pandas DataFrame 
#● Use exception handling for bad data 
#● Use a generator to stream data 
#● Apply decorator to measure execution time 

import time
import functools
import numpy as np
import pandas as pd

# 1. Decorator to measure execution time
def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"⏱️ Execution time for '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# 2. Generator to stream data line by line with Exception Handling
def stream_numeric_data(file_path):
    """Streams rows from a file, handling bad data seamlessly."""
    try:
        with open(file_path, "r") as file:
            for line_num, line in enumerate(file, 1):
                clean_line = line.strip()
                if not clean_line:
                    continue  # Skip empty lines
                try:
                    # Convert string input into a float
                    yield float(clean_line)
                except ValueError:
                    print(f"⚠️ Warning: Skipped invalid data at line {line_num}: '{clean_line}'")
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")

# 3. Core Processing Pipeline
@timer_decorator
def process_pipeline(file_path):
    """Orchestrates data streaming, NumPy calculations, and Pandas conversion."""
    # Consume data from the generator stream
    data_stream = stream_numeric_data(file_path)
    data_list = list(data_stream)
    
    if not data_list:
        print("❌ No valid numeric data found to process.")
        return pd.DataFrame()

    # NumPy calculations
    data_array = np.array(data_list)
    data_mean = np.mean(data_array)
    data_std = np.std(data_array)
    data_min = np.min(data_array)
    data_max = np.max(data_array)

    # Convert results to Pandas DataFrame
    metrics_summary = {
        "Metric": ["Sample Count", "Mean", "Standard Deviation", "Min Value", "Max Value"],
        "Value": [len(data_array), data_mean, data_std, data_min, data_max]
    }
    
    df_results = pd.DataFrame(metrics_summary)
    return df_results

# --- SIMULATION AND TESTING ---
if __name__ == "__main__":
    # Dynamically creating a dummy file containing valid integers, floats, and bad data
    mock_filename = "sensor_data.txt"
    with open(mock_filename, "w") as f:
        f.write("10.5\n20.3\nINVALID_ROW\n30.1\n40.8\n\n50.2\nCORRUPTED_DATA\n60.4\n")

    print("--- Starting Pipeline Processing ---")
    results_df = process_pipeline(mock_filename)
    
    print("\n--- Final Summary DataFrame ---")
    print(results_df)
