# Calculator


def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    
    
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
        
    should_continue = True

    while should_continue:
        
        operation_symbol = input("Pick an operation from the choices above: ")

        num2 = float(input("What's the second number?: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)
                    
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        choice = input(f"Type (y) to continue calculating with {answer}, type (n) to start a new calculation, or type (e) to exit: ")
        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_continue = False
            print(f"Final answer {answer}")
            print("STARTING NEW CALCULATOR")
            calculator()
        else:
            print(f"Your final answer was {answer}, Bye!")
            should_continue = False
            break
            
calculator()
