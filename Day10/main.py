from art import logo
print(f"{logo}")

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    if n2 == 0:
        print("Cannot divide by 0")
        return n1
    else:
        return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Functionality of the project
first_number = float(input("What's the first number?"))
again = 'y'
result = 0.0

def calculate(n1, operation, n2):
    return operations[operation](n1,n2)
    
while again == 'y':
    
    for o in operations:
        print(o)  
    ope = input("Pick a operation: ")
    second_number = float(input("What's the second number?"))
    
    result = calculate(n1=first_number, operation=ope, n2=second_number)
    print(f'{first_number} {ope} {second_number} = {result}')
    
    first_number = result
    again = input("Want to go again? 'y' or 'n': ")
    
print(f"Final result: {result}")

