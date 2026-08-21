# Employee Management System (OOP + File + Dict) 
#Scenario: 
#Manage employee data. 
#Task: 
#● Create a class Employee 
#● Store employees in a dictionary 
#● Save data to a file 
#● Use exception handling for invalid salary input 
#● Use loop to display all employees 
import json

class Employee:
    """Represents an employee profile with validation logic."""
    def __init__(self, emp_id: str, name: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def to_dict(self):
        """Converts object data into a standard dictionary for storage."""
        return {"name": self.name, "salary": self.salary}


class EmployeeDatabase:
    """Manages the lifecycle, operations, and file storage of employee records."""
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.employees = {} 
        self.load_from_file()

    def add_employee(self):
        """Asks for input, handles errors, and inserts a new employee."""
        print("\n--- Register New Employee ---")
        emp_id = input("Enter Employee ID: ").strip()
        
        if emp_id in self.employees:
            print(f"❌ Error: ID '{emp_id}' already exists!")
            return

        name = input("Enter Employee Name: ").strip()
        if not name:
            print("❌ Error: Name field cannot be empty.")
            return

        try:
            salary_input = input("Enter Base Salary: ").strip()
            salary = float(salary_input)
            
            if salary < 0:
                raise ValueError("Salary metric cannot be negative numbers.")
                
        except ValueError as e:
            print(f"❌ Invalid Input: Please enter a valid positive number. ({e})")
            return

        new_emp = Employee(emp_id, name, salary)
        self.employees[emp_id] = new_emp
        print(f"✓ Employee '{name}' added locally.")
        self.save_to_file()

    def display_all_employees(self):
        """Use loop to display all active employee rows."""
        print("\n=== Active Employee Directory ===")
        if not self.employees:
            print("[Empty Directory: No records found.]")
            return

        for emp_id, emp_obj in self.employees.items():
            print(f"ID: {emp_id:6} | Name: {emp_obj.name:15} | Salary: Rs. {emp_obj.salary:,.2f}")

    def save_to_file(self):
        """Save data to a file in structural JSON notation."""
        try:
            serializable_dict = {uid: obj.to_dict() for uid, obj in self.employees.items()}
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(serializable_dict, file, indent=4)
            print("✓ Database file synced safely to storage disk.")
        except IOError as e:
            print(f"❌ Storage Write Error: Could not save records to disk. {e}")

    def load_from_file(self):
        """Re-hydrate memory data structures on execution launch."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                raw_data = json.load(file)
                self.employees = {
                    uid: Employee(uid, info["name"], info["salary"]) 
                    for uid, info in raw_data.items()
                }
        except FileNotFoundError:
            self.employees = {}
        except (json.JSONDecodeError, KeyError):
            print("⚠️ Diagnostic Warning: Data file corrupted. Starting fresh registry.")
            self.employees = {}



if __name__ == "__main__":
    db = EmployeeDatabase()
    
    while True:
        print("\n==============================")
        print(" EMPLOYEE MANAGEMENT SYSTEM")
        print("==============================")
        print("1. View Employee Registry")
        print("2. Insert New Employee")
        print("3. Terminate Application")
        
        choice = input("\nSelect system action (1-3): ").strip()
        
        if choice == "1":
            db.display_all_employees()
        elif choice == "2":
            db.add_employee()
        elif choice == "3":
            print("\nExiting employee console system. Operations completed.")
            break
        else:
            print("❌ Invalid command entry. Select numbers from 1 to 3.")
