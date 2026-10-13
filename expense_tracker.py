expenses = []

def new_expenses():
    name = input("Write the name of your expense: ")
    amount = float(input("Write the amount of your expense: "))
    category = input("Write the category of your expense: ")
    expense = {
        "Name": name,
        "Amount": amount,
        "Category": category,
    }
    expenses.append(expense)
    print("Expense added successfully")
    
def view_expenses():
    if len(expenses) == 0:
        print("No expense added yet")
    else:       
        for expense in expenses:
            print("Name: ",expense["Name"])
            print("Amount: ",expense["Amount"])
            print("Category: ",expense["Category"])
            print("---------------------------------")
            
def total_expenses():
    total = 0
    for expense in expenses:
        total += expense["Amount"]
    print(total)
    return total
    
def view_category():
    cat = input("Please enter a category: ")
    for expense in expenses:
        if cat.lower() == expense["Category"].lower():
            print(expense)
            
def remaining_budget():
    amt = float(input("Enter the money you have right now: "))
    rem = amt - total_expenses()
    print(rem)
        
    
while True:
        print("=================================\n     Student Expense Tracker\n ================================")
        print("Main Menu")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. View Expenses by Category")
        print("5. Check Remaining Budget")
        print("6. Find Highest Expense")
        print("7.Exit")
        try:
            user = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a specified value")
            continue
        if user == 1:
            new_expenses()
            
        if user == 2:
            view_expenses()
            
        if user == 3:
            total_expenses()
            
        if user == 4:
            view_category()
            
        if user == 5:
            remaining_budget()
            
        if user == 6:
            print(max(expenses,key = lambda s: s["Amount"]))                        
            
        if user == 7:
            print("Thank you for using expense tracker!")
            break
