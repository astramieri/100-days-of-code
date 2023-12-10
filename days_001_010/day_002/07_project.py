print("Welcome to the tip calculator")

total_bill = input("What was the total bill (€)? ")

tip_percentage = input("What percentage tip would you like to give (%)? ")

people_to_split = input("How many people to split the bill? ")

total = round(float(total_bill) * (1 + int(tip_percentage) / 100), 2)

quota = round(total / int(people_to_split), 2)

print(f"Total bill with tip is {total} €")

print(f"Each person should pay {quota} €.")