import os
from art import logo

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

def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))    
    
    while True:
        operation = input("Which operation do you want to do ('+', '-', '*', '/')? ")

        num2 = float(input("What's the next number? "))

        result = operations[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        num1 = result

        next_action = input("Do you want continue ('y'=yes, 'r'=reset, 'n'=exit)? ")

        if next_action == 'n':
            break
        elif next_action == 'r':
            os.system('cls')
            calculator()

calculator()