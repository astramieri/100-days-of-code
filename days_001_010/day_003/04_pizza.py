# Thank you for choosing Python Pizza Deliver

print("Thank you for choosing Python Pizza Deliveries!")

# collecting preferences
size = input("What size pizza do you want? (S or M or L) ")
pepperoni = input("Do you want pepperoni on it? (Y or N) ")
extra_cheese = input("Do you want extra cheese on it? (Y or N) ")

# inizialize bill
total_bill = 0

if size == "S": # small pizza
    total_bill += 15
elif size == "M": # medium pizza
    total_bill += 20
elif size == "L": # large pizza
    total_bill += 25

if pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is €{total_bill}.")
        

