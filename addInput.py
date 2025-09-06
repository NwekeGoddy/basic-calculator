# Question: Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

# number1 = int(input("Enter the first integer: "));
# number2 = int(input("Enter the second integer: "));
# number3 = int(input("Enter the third integer: "));

# print(f"The addition of {number1} , {number2}, and {number3}  is {number1 + number2 + number3}");


numbers = [];

num_of_input = eval(input("Enter the number of integer you wish to enter: "));


for i in range(num_of_input):
     number = int(input(f"Enter the integer {i+1}: "));
     numbers.append(number);

total_sum = sum(numbers);
print(f"The sum of all the integers enter is {total_sum}");
    