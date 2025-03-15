def perform_operation():
    # Ask the user for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Ask the user for an operation
    operation = input("Enter the operation (e.g., +, -, *, /): ")

    # Validate the operation input
    if operation in ('+', '-', '*', '/') and operation != '/':  # Avoid division by zero
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero!")
                return
        print(f"The result is: {result}")
    else:
        print("Invalid operation. Please enter a valid operation (+, -, *, /).")

# Call the function
perform_operation()