def max_of_three():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    if num1>= num2 and num1 >= num3:
        return num1
    elif num2>= num1 and num2 >= num3:
        return num2
    else:
        return num3
max_number = max_of_three()
print(f"The maximum number is: {max_number}")
