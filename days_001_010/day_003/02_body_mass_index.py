# BMI = Body Mass Index

height = input("What is your height in meters (m)? ")
weight = input("What is your weight in kilograms (kg)? ")

bmi = round(float(weight) / (float(height) ** 2), 2)

bmi_format = "{:.2f}".format(bmi)

if bmi <= 18.5:
    print(f"Your BMI is: {bmi_format}. You are underweight.")
elif bmi <= 25:
    print(f"Your BMI is: {bmi_format}. You have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is: {bmi_format}. You are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is: {bmi_format}. You are obese.")
else:
    print(f"Your BMI is: {bmi_format}. You are clinically obese.")