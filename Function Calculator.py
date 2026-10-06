# 4 function for the basic arithmetic operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

try:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if num2 == 0:
        raise ZeroDivisionError
    
except ValueError as ve:
    print(ve)

except ZeroDivisionError as ze:
    print(ze)
 
    
else:
    
    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
    
    




