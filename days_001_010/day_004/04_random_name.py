import random

names = "Peter, Ben, Natasha, Jim"

names_list = names.split(", ")

print(names_list)

random_int = random.randint(1, len(names_list) - 1)

random_name = names_list[random_int]

print(f"{random_name} is going to pay for the lunch!")