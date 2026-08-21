# Shopping Cart System 
#Scenario: A user adds items to a shopping cart. 
#Task: 
#● Store items in a list 
#● Convert to set to remove duplicates 
#● Use loop + condition to calculate total cost 
#● Handle invalid input using try-except 

PRICE_LOOKUP = {
    "apple": 1.50,
    "banana": 0.75,
    "milk": 3.20,
    "bread": 2.50,
    "coffee": 8.99
}

shopping_cart = ["apple", "banana", "milk", "apple", "bread", "banana", "coffee", "xyz"]

print(f"Original Cart (List): {shopping_cart}")

unique_items = set(shopping_cart)
print(f"Unique Items (Set): {unique_items}\n")

total_cost = 0.0

print("--- Processing Checkout ---")
for item in unique_items:
    try:
        
        cleaned_item = item.strip().lower()
        
        if cleaned_item not in PRICE_LOOKUP:
            raise KeyError(f"'{item}' is not available in our store catalog.")
            
        item_price = PRICE_LOOKUP[cleaned_item]
        total_cost += item_price
        print(f"Added {cleaned_item.capitalize()}: Rs. {item_price:.2f}")
        
    except KeyError as error:
        print(f"Error: {error} Skipping item.")

print("\n--- Final Receipt ---")
print(f"Total Checkout Cost: Rs. {total_cost:.2f}")
