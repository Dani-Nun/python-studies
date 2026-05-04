# Personal Finance Tracker
# A command-line tool to track income and expenses

transactions = []

def add_transaction(type, category, amount, description):
    transaction = {
        "type": type,
        "category": category,
        "amount": amount,
        "description": description
    }
    transactions.append(transaction)
    print(f"Transaction added: {description} — ${amount:.2f}")

def calculate_balance():
    income = 0
    expenses = 0
    for t in transactions:
        if t["type"] == "income":
            income += t["amount"]
        else:
            expenses += t["amount"]
    return income, expenses, income - expenses

def show_summary():
    income, expenses, balance = calculate_balance()
    print("\n--- Financial Summary ---")
    print(f"Total Income:   ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Balance:        ${balance:.2f}")
    if balance > 0:
        print("Status: Positive")
    elif balance == 0:
        print("Status: Neutral")
    else:
        print("Status: Negative")

def show_transactions():
    if not transactions:
        print("No transactions yet.")
        return
    print("\n--- All Transactions ---")
    for i, t in enumerate(transactions, 1):
        symbol = "+" if t["type"] == "income" else "-"
        print(f"{i}. [{symbol}] {t['description']} | {t['category']} | ${t['amount']:.2f}")

def main():
    print("=== Personal Finance Tracker ===")
    while True:
        print("\n1. Add income")
        print("2. Add expense")
        print("3. Show summary")
        print("4. Show all transactions")
        print("5. Exit")
        choice = input("\nChoose an option: ")
        if choice == "1":
            desc = input("Description: ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            add_transaction("income", category, amount, desc)
        elif choice == "2":
            desc = input("Description: ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            add_transaction("expense", category, amount, desc)
        elif choice == "3":
            show_summary()
        elif choice == "4":
            show_transactions()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()