import csv
import json
import os
from colorama import init, Fore, Style
init(autoreset=True)
EXPENSES_FILE ="expenses.csv"
BUDGET_FILE = "budget.json"

def initialize_csv():
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["date","category","description","amount"])

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (DD/MM/YYYY): ")
    
    categories = ["Food", "Transport", "Shopping", "Groceries", "Other"]
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    cat_choice = input("Choose category (1-5): ")
    
    try:
        category = categories[int(cat_choice) - 1]
    except:
        print(Fore.RED + "Invalid choice, setting to Other")
        category = "Other"
    
    description = input("Enter description: ")
    amount = input("Enter amount (€): ")

    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print(Fore.GREEN + "\n Expense added successfully!")

def view_expenses():
    print("\n--- All Expenses ---")
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        expenses = list(reader)
    if not expenses:
        print(Fore.RED + "No expenses found!")
        return
    print(f"\n{'No.':<5}{'Date':<15}{'Category':<15}{'Description':<25}{'Amount(€)':<10}")
    print("-"*70)
    for i, row in enumerate(expenses, 1):
        print(f"{i:<5} {row['date']:<15} {row['category']:<15} {row['description']:<25} {row['amount']:<10}")
def load_budget():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE,"r") as file:
            return json.load(file)
    return {"total": 0, "categories":{}}

def set_budget():
    print("\n---Set your Budget ---")
    total= float(input("Enter your total monthly budget(€): "))
    categories = ["Food", "Transport", "Shopping", "Groceries","Other"]
    category_budgets = {}
    print("\nNow set a limit for each category:")
    for category in categories:
        amount = float(input(f"  {category} budget (€): "))
        category_budgets[category] = amount
    category_total = sum(category_budgets.values())

    if category_total > total:
        print(Fore.RED + f"\n Warning: Your category budgets (€{category_total}) exceed your total budget (€{total})!")
        confirm = input("Do you still want to save? (yes/no): ")
        if confirm.lower() != "yes":
            print(Fore.RED + "Budget not saved. Please try again.")
            return
    
    
    budget = {
        "total": total,
        "categories": category_budgets
    }
    
    with open(BUDGET_FILE, "w") as file:
        json.dump(budget, file, indent=4)
    
    print(Fore.GREEN + "\n Budget saved successfully!")

def show_summary():
    print("\n--- Spending Summary ---")
    
    # Load expenses
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        expenses = list(reader)
    
    if not expenses:
        print(Fore.RED + "No expenses found!")
        return
    
    # Load budget
    budget = load_budget()
    total_budget = budget["total"]
    category_budgets = budget["categories"]
    
    # Calculate total spent
    total_spent = sum(float(row["amount"]) for row in expenses)
    
    # Calculate spent per category
    category_spent = {}
    for row in expenses:
        cat = row["category"]
        category_spent[cat] = category_spent.get(cat, 0) + float(row["amount"])
    
    # Total budget summary
    print(f"\n{'='*40}")
    print(f"Total Budget:  €{total_budget:.2f}")
    print(f"Total Spent:   €{total_spent:.2f}")
    print(f"Remaining:     €{total_budget - total_spent:.2f}")
    
    percentage = (total_spent / total_budget * 100) if total_budget > 0 else 0
    
    if percentage >= 100:
        print(Fore.RED + f"  You have exceeded your total budget! ({percentage:.1f}%)")
    elif percentage >= 75:
        print(Fore.YELLOW + f"  Warning: You have used {percentage:.1f}% of your total budget!")
    else:
        print(Fore.GREEN + f" You are within budget! ({percentage:.1f}% used)")
    
    # Category breakdown
    print(f"\n{'Category':<15}{'Spent':>10}{'Budget':>10}{'Remaining':>12}{'Status'}")
    print("-" * 60)
    
    for category in ["Food", "Transport", "Shopping", "Groceries", "Other"]:
        spent = category_spent.get(category, 0)
        cat_budget = category_budgets.get(category, 0)
        remaining = cat_budget - spent
        percentage_cat = (spent / cat_budget * 100) if cat_budget > 0 else 0
        
        if percentage_cat >= 100:
            status = Fore.RED + "EXCEEDED"
        elif percentage_cat >= 75:
            status = Fore.YELLOW + "WARNING"
        else:
            status = Fore.GREEN + "OK"
        
        print(f"{category:<15}€{spent:>8.2f}  €{cat_budget:>7.2f}  €{remaining:>9.2f}  {status}")
    
    # Most expensive category
    if category_spent:
        most_expensive = max(category_spent, key=category_spent.get)
        print(f"\n💸 Most spent category: {most_expensive} (€{category_spent[most_expensive]:.2f})")

def main() :
    initialize_csv()
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add expense")
        print("2. View All expenses")
        print("3. Set Budget")
        print("4. Show Summary")
        print("5. Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
           set_budget()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Goodbye!!")
            break
        else:
            print(Fore.RED + "Invalid option, try again.")

if __name__ == "__main__":
    main()