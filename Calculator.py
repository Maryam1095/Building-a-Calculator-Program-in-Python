#Addition function
def add(num1,num2):
    return num1 + num2
#Substraction function
def subtract(num1, num2):
    return num1 - num2
# Multiplication function
def multiply(num1, num2):
    return num1 * num2
# Division function
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Print available operation symbols using a for loop
print("Available operation symbols:")
for symbol in operations.keys():
    print(symbol)

    # Prompt the user to enter the first number
    num1 = float(input("Enter the first number: "))
    # Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))

    while True:

        # Get the operation from the user
        operation = input("Select an operation (+, -, *, /): ")

        # Retrieve the corresponding function from the dictionary
        calculation_function = operations[operation]

        # Perform the calculation and store the result
        answer = calculation_function(num1, num2)

        # Print the equation and the result
        print(f"{num1} {operation} {num2} = {answer}")

        # Ask the user if they would like to continue using the result
        choice = input("Continue using the result (Y/N)? ")
        if choice.upper() == "Y":
            # Update num1 with the result for further calculations
            num1 = answer
            num2 = float(input("Enter the second number: "))

        else:
            # Prompt the user to enter the first number
            num1 = float(input("Enter the first number: "))
            # Prompt the user to enter the second number
            num2 = float(input("Enter the second number: "))

