def calculator():
    operator = input("Enter an operator (+, -, *, /): ")
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    if operator == '+':
        print("Result:", first + second)
    elif operator == '-':
        print("Result:", first - second)
    elif operator == '*':
        print("Result:", first * second)
    elif operator == '/':
        if second != 0:
            print("Result:", first / second)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operator")
calculator()
