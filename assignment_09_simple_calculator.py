# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# -----------------------------------------------------------------------------
# ARITHMETIC OPERATION FUNCTIONS
# -----------------------------------------------------------------------------
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Returns the quotient of two numbers rounded to 2 decimal places.
    Raises ZeroDivisionError if b is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return round(a / b, 2)


def modulus(a, b):
    """
    Returns the remainder of division of two numbers.
    Raises ZeroDivisionError if b is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulus by zero.")
    return a % b


def power(a, b):
    """Returns 'a' raised to the power of 'b'."""
    return a**b


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def get_number_input(prompt):
    """
    Safely prompts the user for a numeric input (float or int).
    Retries until a valid number is entered.
    """
    while True:
        try:
            val = float(input(prompt))
            # Return as integer if it's a whole number (e.g., 10.0 -> 10)
            return int(val) if val.is_integer() else val
        except ValueError:
            print("  -> Error: Invalid input. Please enter a valid number.")


def display_menu():
    """Prints the main calculator menu choices."""
    print("\n" + "=" * 28)
    print("     SIMPLE CALCULATOR")
    print("=" * 28)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


# -----------------------------------------------------------------------------
# MAIN PROGRAM LOOP
# -----------------------------------------------------------------------------
def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("\nGoodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Error: Invalid option. Please select a choice between 1 and 7.")
            continue

        # Get numeric inputs
        num1 = get_number_input("Enter first number : ")
        num2 = get_number_input("Enter second number: ")

        # Perform calculation based on choice
        try:
            if choice == "1":
                result = add(num1, num2)
                symbol = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                symbol = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                symbol = "*"
            elif choice == "4":
                result = divide(num1, num2)
                symbol = "/"
            elif choice == "5":
                result = modulus(num1, num2)
                symbol = "%"
            elif choice == "6":
                result = power(num1, num2)
                symbol = "**"

            print(f"Result: {num1} {symbol} {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
# =============================================================================

