#Samantha Trejo< Error Handling Calculator

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def main():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = input("Enter the operation (+, -, *, /): ")

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
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
        return

    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
