# Q:A user wants to save grocery items in a file grocery.txt. Write a Python program that 
#takes multiple items from the user and writes them into the file, with each item on a 
#new line.
with open("grocery.txt", "w") as file:
    print("Enter your grocery items. Type 'done' when you are finished.")
    
    while True:
        item = input("Enter item: ").strip()
        if item.lower() == "done":
            break
        if not item:
            print("Item name cannot be empty. Please try again.")
            continue
        file.write(item + "\n")

print("\nSuccess! Your grocery items have been saved to 'grocery.txt'.")
