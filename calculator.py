# 1. Define the core math functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# 2. Define the action function using Python's match-case
def action(choice, n1, n2):
    match choice:
        case 1:
            result = add(n1, n2)
            print(f"Result: {n1} + {n2} = {result}")
        case 2:
            result = sub(n1, n2)
            print(f"Result: {n1} - {n2} = {result}")
        case 3:
            result = mul(n1, n2)
            print(f"Result: {n1} * {n2} = {result}")
        case 4:
            result = div(n1, n2)
            print(f"Result: {n1} / {n2} = {result}")
        case _:
            print("Invalid choice! Please select a number between 1 and 4.")

# 3. Display a menu to the user so they know what to choose
print("--- Simple Calculator ---")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("-------------------------")

# 4. Take inputs from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = int(input("Enter your choice (1-4): "))

# 5. Run the calculator action
action(choice, num1, num2)