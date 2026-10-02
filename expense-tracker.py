# Expense Tracker - by Success Brownson
balance = 0
history = []

def add_income(amount, desc):
    global balance
    balance += amount
    history.append(f"+ N{amount} - {desc}")
    print(f"Income: N{amount} - {desc}")

def add_expense(amount, desc):
    global balance
    if amount > balance:
        print(f"Failed: Not enough balance for {desc}")
    else:
        balance -= amount
        history.append(f"- N{amount} - {desc}")
        print(f"Expense: N{amount} - {desc}")

print("=== SUCCESS EXPENSE TRACKER ===\n")
add_income(10000, "Salary")
add_income(2000, "Freelance")
add_expense(500, "Airtel Airtime")
add_expense(1500, "Food")
add_expense(700, "Transport")

print(f"\nFINAL BALANCE: N{balance}")
print("\nHISTORY:")
for h in history:
    print(h)