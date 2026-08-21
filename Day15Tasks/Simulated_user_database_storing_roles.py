# Decorator-based Access Control 
#Scenario: 
#Restrict access to certain functions. 
#Task: 
#● Create a decorator to check user role 
#● Use condition inside decorator 
#● Apply decorator to multiple functions 
#● Store roles in a dictionary
# Simulated user database storing roles
USER_ROLES = {
    "alice": "admin",
    "bob": "manager",
    "charlie": "employee",
    "guest_user": "guest"
}

def require_role(allowed_roles):
    """Decorator factory to restrict access based on user roles."""
    def decorator(func):
        def wrapper(username, *args, **kwargs):
            # Fetch user role or default to guest
            user_role = USER_ROLES.get(username, "guest")
            
            # Condition check inside the decorator
            if user_role in allowed_roles:
                return func(username, *args, **kwargs)
            else:
                return f"Access Denied for '{username}'. Role '{user_role}' lacks permission."
        return wrapper
    return decorator

# Applying the decorator to multiple functions

@require_role(["admin"])
def delete_database(username):
    return f"Success: {username} deleted the database."

@require_role(["admin", "manager"])
def view_financials(username):
    return f"Success: {username} viewed financial reports."

@require_role(["admin", "manager", "employee"])
def view_dashboard(username):
    return f"Success: {username} viewed the employee dashboard."

# Execution examples
print(delete_database("alice"))    # Admin allowed
print(delete_database("bob"))      # Manager denied
print(view_financials("bob"))     
print(view_dashboard("charlie"))  
print(view_dashboard("guest_user"))
