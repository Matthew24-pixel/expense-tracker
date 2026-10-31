# Project: Expense Tracker | Installment 1
# Author: <Matthew Jerard P. Garcia>
# A simple landing page for a personal expense tracker.

LINE = "=" * 40

print(LINE)
print("EXPENSE TRACKER")
print("Know where your money goes.")
print(LINE)

print()
print("Welcome! This is your personal expense tracker.")
print()

print("MAIN MENU")
print("  [1] Add an expense          (coming soon)")
print("  [2] View all expenses       (coming soon)")
print("  [3] Show total spent        (coming soon)")
print("  [4] Exit                    (coming soon)")

print()
print(LINE)
print("Made by : <Matthew Jerard P. Garcia>   |   Installment 1")
print(LINE)

name = input("\nWelcome, what should we call you? ")
print(f"Welcome, {name}! Let's log two expenses.\n")
item1 = input("What's your first item? ")
amount1 = float(input("What's the amount? "))
subtotal += amount1
item2 = input("What's your second item? ")
amount2 = float(input("What's the amount? "))
subtotal += amount2
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print('\n' + '-' * 40)
print("SUMMARY")
print(f"  - {item1}:\t\t\t${amount1:.1f}")
print(f"  - {item2}:\t\t\t${amount2:.1f}")
print(f"Subtotal:\t\t\t${subtotal:.1f}")
print(f"Average:\t\t\t${average:.1f}")
print(f"Tax ({tax_percent:.1f}%):\t\t\t${tax:.1f}")
print(f"Grand total:\t\t\t${total:.1f}")
print(f"Over budget?\t\t\t{over_budget}")
print(f"Left in budget:\t\t\t${left:.1f}")
print('-' * 40)
print("Made by: Matthew Jerard P. Garcia | Installment 3")