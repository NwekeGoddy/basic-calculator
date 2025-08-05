first_number = input("Enter the first number");
second_number = input("Enter the second number");
operator = input("Enter the operator");

try:
    result = eval(f"{first_number} {operator} {second_number}")
    print(f"{first_number} {operator} {second_number} = {result}")
except ZeroDivisionError:
    print("Error! Division by zero.")
except Exception as e:
    print(f"Invalid input: {e}")