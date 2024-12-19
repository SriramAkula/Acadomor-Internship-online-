import os

expenses = []

def add_expense():
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., food, transportation): ")
    expenses.append({"description": description, "amount": amount, "category": category})
    print(f"Added: {description} - ${amount} in {category} category.\n")

def view_expenses_by_category():
    category = input("Enter the category to view expenses: ")
    found = False
    print(f"\nExpenses in category '{category}':")
    for i, expense in enumerate(expenses):
        if expense["category"] == category:
            print(f"{i+1}. {expense['description']} - ${expense['amount']}")
            found = True
    if not found:
        print("No expenses found in this category.\n")

def calculate_total_expenses():
    totals = {}
    for expense in expenses:
        category = expense['category']
        if category in totals:
            totals[category] += expense['amount']
        else:
            totals[category] = expense['amount']
    
    print("\nTotal expenses by category:")
    for category, total in totals.items():
        print(f"{category}: ${total}")
    print()

def save_to_file():
    with open('expenses.txt', 'w') as file:
        for expense in expenses:
            file.write(f"{expense['description']},{expense['amount']},{expense['category']}\n")
    print("Expenses saved to file.\n")

def load_from_file():
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            for line in file:
                description, amount, category = line.strip().split(',')
                expenses.append({"description": description, "amount": float(amount), "category": category})
        print("Expenses loaded from file.\n")
    else:
        print("No file found. Starting with an empty list of expenses.\n")

def main_menu():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses by Category")
        print("3. Calculate Total Expenses")
        print("4. Save and Exit")
        print("5. Load Expenses from File")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses_by_category()
        elif choice == '3':
            calculate_total_expenses()
        elif choice == '4':
            save_to_file()
            break
        elif choice == '5':
            load_from_file()
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main_menu()
