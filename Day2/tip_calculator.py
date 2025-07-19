print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? R$"))
tip = int(input("What's the percentage of the waiter?"))
people = int(input("How many people to split the bill?"))

percentual_bill = bill * (tip/100)
total_for_each = (bill + percentual_bill) / people

print(f"Each one should pay: {round(total_for_each, 2)}")