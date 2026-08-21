# Basic File Logger 
#Scenario: 
#A system logs user actions. 
#Task: 
#● Take user input 
#● Store logs in a file 
#● Use loop to allow multiple entries 
#● Handle file errors using exception handling 

import datetime

print("=== System Action Logger ===")
print("Type your actions to log them. Type 'exit' to quit the program.\n")

while True:
    try:
        
        user_action = input("Enter user action to log: ").strip()
        
    
        if user_action.lower() == 'exit':
            print("Exiting logger system. Goodbye!")
            break
            
        
        if not user_action:
            print("Empty action skipped. Please enter text.")
            continue

        
        with open("system_activity.log", "a", encoding="utf-8") as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] {user_action}\n")
            print("✓ Action successfully logged.\n")

    except PermissionError:
        print("❌ Critical Error: Permission denied. Cannot write to file. Check folder permissions.\n")
    except FileNotFoundError:
        print("❌ Critical Error: Target directory for the log file does not exist.\n")
    except OSError as e:
        print(f"❌ System Error: A disk or system error occurred: {e}\n")
