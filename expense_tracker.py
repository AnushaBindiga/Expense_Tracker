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

def main():
    initialize_csv()
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add expense")
        print("2. Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option, try again.")

if __name__ == "__main__":
    main()