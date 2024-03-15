# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y


def power(x, y):
    return x ** y


while True:
    try:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Exit")

        choice = int(input("Enter choice (1/2/3/4/5/6): "))

        if choice in (1, 2, 3, 4, 5):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
        elif choice == 5:
            print("Result:", power(num1, num2))
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An error occurred:", e)
