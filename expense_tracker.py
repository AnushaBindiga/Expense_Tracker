import csv
import os
from colorama import init, Fore, Style
init(autoreset=True)
EXPENSES_FILE ="expenses.csv"

def initialize_csv():
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILe, mode='w',newlinw='') as file:
            writer = csv.writer(file)
            writer.writerow(["date","category","description","amount"])

def add_expense():
    print("\n--- Add New Expense---")
    date = input("Enter date (DD/MM/YYYY):")
    print("Categories: Food / Transport / Shopping / Groceries / Other")
    category = input("Enter Category:")
    description = input("Enter description: ")
    amount = input("Enter amount (€):")

    with open(EXPENSES_FILE, mode='a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date,category,description,amount])

    print(Fore.GREEN + "\n Expense added successfully!!")

def view_expenses():
    print("\n--- All Expenses ---")
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        expenses = list(reader)
    if not expenses:
        print(Fore.RED + "No expenses found!")
        return
    print(f"n{'No.':<5}{'Date':<15}{'Category':<15}{'Description':<25}{'Amount(€)':<10}")
    print("-"*70)
    for i, row in enumerate(expenses, 1):
        print(f"{i:<5} {row['date']:<15} {row['category']:<15} {row['description']:<25} {row['amount']:<10}")

def main():
    initialize_csv()
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add expense")
        print("2. View All expenses")
        print("3. Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!!")
            break
        else:
            print(Fore.RED + "Invalid option, try again.")

if __name__ == "__main__":
    main()