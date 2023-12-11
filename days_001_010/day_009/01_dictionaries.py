# {key: value}
# {key1: value1, key2: value2}

key = "key"
value = 99

# Creating a dictionary
programming = {
    "Bug": "An error",
    "Function": "A piece of code",
    "Loop":"The action of repeating",
    123: 456,
    key: value
}

# Adding new items
programming[True] = False

# Retrieving items
print(programming["Bug"])
print(programming[123])
print(programming[key])
print(programming[True])

# Empty dictionary
empty = {}
empty["Key"] = "123"
empty["Key"] = 123
print(empty["Key"])

# Looping
for key in programming:
    print(f"{key} : {programming[key]}")

print(programming)
 