print("Hello! This program will calculate common arithmetic expressions!")

num1 = int(input("Please enter your first number: "))
op = input("Please select +, -, *, or /: ")
num2 = int(input("Please enter your second number: "))

def calc():
    if op == "+":
        print("Your answer is " + str(num1 + num2))
        return
    elif op == "-":
        print("Your answer is " + str(num1 - num2))
        return
    elif op == "*":
        print("Your answer is " + str(num1 * num2))
        return
    elif op == "/":
        print("Your answer is " + str(num1 / num2))
        return
    else:
        return "Please enter a valid operator."

calc()