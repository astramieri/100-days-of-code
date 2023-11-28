# BMI = Body Mass Index

height = input("What is your height in meters (m)? ")
weight = input("What is your weight in kilograms (kg)? ")

bmi = int(float(weight) / (float(height) ** 2)) # conver to whole number

print("Your Body Mass Index (BMI) is: " + str(bmi))