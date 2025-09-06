first_number = input("Enter the first number")
second_number = input("Enter the second number")
operator = input("Enter the operator")

try:
    num1 = float(first_number)
    num2 = float(second_number)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2
    else:
        raise ValueError("Unsupported operator")

    print(f"{num1} {operator} {num2} = {result}")
except ZeroDivisionError:
    print("Error! Division by zero.")
except ValueError as e:
    print(f"Invalid input: {e}")
