

# Calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide 
}

# e.g.
num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

operation = input("Which operation do you want to do ('+', '-', '*', '/')? ")

function = operations[operation]
result = function(num1, num2)

print(f"{num1} {operation} {num2} = {result}")

while True:
    want_continue = input("Do you want continue ('y'=yes, 'n'=no)? ")

    if want_continue == 'n':
        break

    operation = input("Pick another operation ('+', '-', '*', '/')? ")
    num3 = int(input("What's the next number? "))

    function = operations[operation]
    previous = result

    result = function(previous, num3)

    print(f"{previous} {operation} {num3} = {result}")