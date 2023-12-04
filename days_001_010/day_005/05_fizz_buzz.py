target = 100

for i in range (1, target + 1):
    message = ""

    if i % 3 == 0:
        message += "Fizz"
    if i % 5 == 0:
        message += "Buzz"

    if not message:
        message = str(i)

    print(message)