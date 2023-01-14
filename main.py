from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number\n"))
    for k in operation:
        print(k)
    calculator_run = True
    while calculator_run:
        operation_symbol = input("Enter an operation symbol\n")
        num2 = float(input("What's the next number\n"))
        output = operation[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {output}")

        choice = input(f"Do you want to do more operations with {output}, Enter 'y/n for a new calcualtion'\n")
        if choice == 'y':
            num1 = output
        else:
            calculator_run = False
            calculator()


calculator()
