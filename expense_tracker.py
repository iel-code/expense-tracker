import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []


while True:
    print()
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View expenses by category")
    print("4. Show total spending")
    print("5. Delete expenses")
    print("6. Exit")
    
    pick = input("Enter 1-6: ")

    if pick == "1":
        expense_name = input("Enter the expense: ")
        try:
            amount = input("Enter the amount in IDR: ")
            int(amount)
            category = input("Enter the category: ")
            date = input("Enter the date: ")
            print("Adding expense...")
            expenses.append({"name": expense_name, "amount": amount, "category": category, "date": date})
            print(f"Added {expense_name} successfully!")
        except ValueError:
            print("That is not a number!")
    elif pick == "2":
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['name']} - {expense['amount']} - {expense['category']} - {expense['date']}")
    elif pick == "3":
        view_category = input("Which category you want to view: ")
        found = False
        for expense in expenses:
            if view_category.lower() == expense['category'].lower():
                print(f"{expense['name']} - {expense['amount']} - {expense['date']}")
                found = True
        if not found:
            print(f"No expenses found in category {view_category}")
    elif pick == "4":
        total = 0
        for expense in expenses:
            total += int(expense['amount'])
        print(f"The total expenses is {total} IDR")
    elif pick == "5":
        found = False
        delete = input(f"Enter the expense you want to delete: ")
        for expense in expenses:
            if delete.lower() == expense['name'].lower():
                expenses.remove(expense)
                print(f"{delete} is deleted from the expenses!")
                found = True
                break
        if not found:
            print(f"{delete} is not in the expenses list!")
    elif pick == "6":
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
        print()
        print("Good Bye!")
        break