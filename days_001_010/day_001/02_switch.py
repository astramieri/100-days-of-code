first_name = input("What is you name ? ")
last_name = input("What is your last name ? ")

middle_name = first_name
first_name = last_name
last_name = middle_name

print("Welcome, " + first_name + " " + last_name)

first_name, last_name = last_name, first_name # cool

print("Ops sorry, " + first_name + " " + last_name)