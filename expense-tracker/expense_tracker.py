# expense_tracker.py

def add_expense(item, amount):
    with open("expenses.txt", "a", encoding="utf-8") as file:
        file.write(f"{item} - ₹{amount}\n")

def view_expenses():
    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
            data = file.readlines()
            if not data:
                print("📭 No expenses found.")
            else:
                print("\n💰 Expense History:")
                for line in data:
                    print(line.strip())
    except FileNotFoundError:
        print("🗂️ No expense file yet. Add one first.")

print("💸 Expense Tracker App")
while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        item = input("Expense Item: ")
        amount = input("Amount (₹): ")
        add_expense(item, amount)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid input!")
