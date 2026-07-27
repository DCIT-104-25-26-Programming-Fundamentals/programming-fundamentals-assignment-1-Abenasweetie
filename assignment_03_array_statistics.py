# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
def calculate_sum(numbers):
    """Calculates the sum of all elements in a list using a loop."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculates the average of elements in a list."""
    if not numbers:
        return 0.0
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Finds the maximum value in a list using a loop."""
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val


def find_minimum(numbers):
    """Finds the minimum value in a list using a loop."""
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    count = int(input("How many numbers? "))
    
    # Requirement: N must be a positive integer (> 0)
    if count <= 0:
        print("Error: Please enter a positive integer greater than 0.")
    else:
        numbers_list = []
        for i in range(1, count + 1):
            val = float(input(f"Enter number {i}: "))
            
            # Format integer inputs nicely if whole numbers are passed
            if val.is_integer():
                val = int(val)
                
            numbers_list.append(val)
        
        # Calculate results using functions
        total = calculate_sum(numbers_list)
        avg = calculate_average(numbers_list)
        maximum = find_maximum(numbers_list)
        minimum = find_minimum(numbers_list)
        
        # Display output
        print("\nResults:")
        print(f"Sum:     {total}")
        print(f"Average: {avg}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
# =============================================================================

