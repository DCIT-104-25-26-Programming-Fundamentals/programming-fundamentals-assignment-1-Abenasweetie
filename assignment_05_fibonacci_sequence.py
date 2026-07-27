# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================

# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
def print_fibonacci_terms(n):
    """
    Generates and prints the first N terms of the Fibonacci sequence.
    """
    if n <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return

    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    # Print the terms on a single line separated by spaces
    print(f"Fibonacci sequence: {' '.join(map(str, sequence))}")


# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
def is_fibonacci_number(num):
    """
    Determines whether a given number belongs to the Fibonacci sequence.
    Returns True if it is a Fibonacci number, False otherwise.
    """
    if num < 0:
        return False

    # 0 and 1 are the starting points of the Fibonacci sequence
    a, b = 0, 1

    # Generate Fibonacci numbers iteratively until we reach or pass 'num'
    while a < num:
        a, b = b, a + b

    # If 'a' equals 'num', it is in the sequence
    return a == num


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("        FIBONACCI SEQUENCE GENERATOR & CHECKER")
    print("=" * 60)

    # --- TESTING PART A ---
    print("\n>>> PART A: First N Terms <<<")
    try:
        n_terms = int(input("How many terms? "))
        print_fibonacci_terms(n_terms)
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

    # --- TESTING PART B ---
    print("\n>>> PART B: Fibonacci Number Check <<<")
    try:
        check_num = int(input("Enter a number to check: "))

        if is_fibonacci_number(check_num):
            print(f"{check_num} is a Fibonacci number.")
        else:
            print(f"{check_num} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
# =============================================================================

