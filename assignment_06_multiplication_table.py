# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================

# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
def print_single_table(num):
    """
    Prints the multiplication table for a given number from 1 to 12.
    """
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        # Uses formatting to keep columns aligned neatly
        print(f"{num:2d}  x  {i:2d}  =  {num * i:3d}")


# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
def print_range_tables(n):
    """
    Prints the full multiplication tables for every number from 1 to N.
    Uses print_single_table() to print each individual table.
    """
    for current_num in range(1, n + 1):
        print_single_table(current_num)

        # Print a separator line between tables, except after the last one
        if current_num < n:
            print("-" * 27)


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("           MULTIPLICATION TABLE GENERATOR")
    print("=" * 60)

    # --- TESTING PART A ---
    print("\n>>> PART A: Single Multiplication Table <<<")
    try:
        user_num = int(input("Enter a number: "))
        if user_num <= 0:
            print("Error: Please enter a positive integer greater than 0.")
            return
        print_single_table(user_num)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return

    # --- TESTING PART B ---
    print("\n>>> PART B: Tables from 1 to N <<<")
    try:
        n_limit = int(input("Enter a number N: "))
        if n_limit <= 0:
            print("Error: Please enter a positive integer greater than 0.")
            return

        print_range_tables(n_limit)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
# =============================================================================

