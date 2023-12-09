
def greet():
    print(f"Hello!")
    print(f"How do you do?")
    print(f"Isn't the wheater nice today?")


def greet_with_name(name): # parameter is the name of that data
    print(f"Hello, {name}!")
    print(f"How do you do, {name}?")
    print(f"Isn't the wheater nice today?")

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")

greet()

greet_with_name("Angelo") # argument is the actual value of data

greet_with("Angelo", "Mantova") # positional arguments (default)
greet_with(location="Mantova", name="Angelo") # keyword arguments