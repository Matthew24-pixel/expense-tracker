# Expense Tracker
# Author: Matthew Jerard P. Garcia


def print_menu():
    print()
    print("MAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses")
    print("  [3] Show total spent")
    print("  [4] Exit")
    print()


def print_summary(name, subtotal, tax_percent, budget, expenses):
    tax = subtotal * (tax_percent / 100)
    total = subtotal + tax
    left = budget - total
    over_budget = total > budget

    print()
    print("-" * 40)
    print("SUMMARY")
    for item, amount in expenses:
        print(f"  - {item}:\t${amount:.2f}")
    print(f"Subtotal:\t\t${subtotal:.2f}")
    print(f"Tax ({tax_percent:.1f}%):\t${tax:.2f}")
    print(f"Grand total:\t\t${total:.2f}")

    if over_budget:
        print(f"Over budget by ${total - budget:.2f}!")
    elif total > budget * 0.90:
        print(f"Careful: only ${left:.2f} left.")
    else:
        print(f"Within budget. ${left:.2f} left.")

    print("-" * 40)
    print(f"Made by: {name} | Installment 5")


def main():
    print("=" * 40)
    print("             EXPENSE TRACKER")
    print("         Know where your money goes.")
    print("=" * 40)

    name = input("What's your name? ").strip() or "Guest"
    tax_percent = float(input("Tax rate %? "))
    budget = float(input("Your budget? "))

    print(f"Welcome, {name}!")

    subtotal = 0.0
    expenses = []
    choice = ""

    while choice != "4":
        print_menu()
        choice = input("Choose 1-4: ").strip()

        if choice == "1":
            description = input("What was the expense for? ").strip() or "Expense"
            amount = float(input("Amount? "))

            if amount > 200:
                print("  Huge expense - are you sure?")
            elif amount > 100:
                print("  Big expense.")
            elif amount > 50:
                print("  Moderate expense.")
            else:
                print("  Small expense.")

            subtotal += amount
            expenses.append((description, amount))

        elif choice == "2":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print()
                print("EXPENSES")
                for item, amount in expenses:
                    print(f"  - {item}: ${amount:.2f}")

        elif choice == "3":
            print_summary(name, subtotal, tax_percent, budget, expenses)

        elif choice == "4":
            print(f"Goodbye, {name}!")
            print("-" * 40)
            print(f"Made by: {name} | Installment 5")
            print("=" * 40)

        else:
            print("Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
