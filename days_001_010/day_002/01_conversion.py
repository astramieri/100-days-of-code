# Type conversion

name_length = len(input("What is your name? "))

print(type(name_length)) # type check

print("Your name has " + str(name_length) + " characters.") # type casting

var = 123

print(type(int(var)))
print(type(str(var)))
print(type(float(var)))
print(type(bool(var)))
