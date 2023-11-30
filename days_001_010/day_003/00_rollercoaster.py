print("Welcome to the rollercoaster!")

height = int(input("What is your height (cm)? "))

total_bill = 0

if height > 120:
    print("You can rider the rollercoaster!")

    age = int(input("What is your age? "))

    if age < 12:
        total_bill = 5
        print("Child tickets are €5.")
    elif age <= 18:
        total_bill = 7
        print("Youth tickets are €7.")
    else:
        total_bill = 12
        print("Adult tickets are €12.")

    photo = input("Do you want a photo taken? (y or n) ")

    if photo.lower() == "y":
        total_bill += 3

    print(f"Your total bill is €{total_bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")