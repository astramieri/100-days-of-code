# Love Calculator
print("The Love Calculator is calculating your score ...")

name1 = input("What is your name? ")
name2 = input("What is his/her name? ")

names = (name1 + name2).upper()

first_digit = 0
second_digit = 0

first_digit += (names).count("T")
first_digit += (names).count("R")
first_digit += (names).count("U")
first_digit += (names).count("E")

second_digit += (names).count("L")
second_digit += (names).count("O")
second_digit += (names).count("V")
second_digit += (names).count("E")

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go toghether like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score i {score}");
