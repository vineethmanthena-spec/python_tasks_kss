# Generator-based Log Reader 
#Scenario: 
#A large log file needs to be processed. 
#Task: 
#● Create a generator to read file line by line 
#● Use loop to process logs 
#● Use condition to filter errors 
#● Count occurrences using a dictionary 

def log_reader(file_path):
    """Generator to read a file line by line without loading it into memory."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line


def process_logs(file_path):
    """Loops through logs, filters errors, and counts occurrences."""
    error_counts = {}

    for line in log_reader(file_path):
        
        if "ERROR" in line:
            
            error_msg = line.strip()

            if error_msg in error_counts:
                error_counts[error_msg] += 1
            else:
                error_counts[error_msg] = 1

    return error_counts