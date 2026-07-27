# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (Input & Display)
# -----------------------------------------------------------------------------
def get_matrix(rows, cols, name="Matrix"):
    """
    Reads a matrix of size rows x cols from the user.
    Each row is entered on a single line with space-separated values.
    """
    print(f"\nEntering values for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                # Read line, split by spaces, and convert each item to an integer
                row_input = input(f"Enter row {i + 1}: ").strip().split()
                if len(row_input) != cols:
                    print(
                        f"  -> Error: Please enter exactly {cols} numbers separated by spaces."
                    )
                    continue

                row = [int(val) for val in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("  -> Error: Please enter valid integers only.")
    return matrix


def display_matrix(matrix, title="Matrix"):
    """
    Displays a 2D list in a neatly aligned grid format.
    """
    print(f"\n--- {title} ---")
    for row in matrix:
        for val in row:
            # {:4d} formats integers into a right-aligned column of width 4
            print(f"{val:4d}", end=" ")
        print()  # Newline after each row
    print()


# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
def transpose_matrix(matrix):
    """
    Computes and returns the transpose of a given matrix (M x N -> N x M).
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize transposed matrix of size (cols x rows) with zeros
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Use nested loops to flip rows and columns
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
def add_matrices(matrix_a, matrix_b):
    """
    Computes element-wise sum of two matrices of identical size (M x N).
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    # Initialize result matrix of size (rows x cols)
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Nested loops to add corresponding elements
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b):
    """
    Multiplies Matrix A (M x N) by Matrix B (N x P).
    Returns result matrix of size (M x P).
    """
    m = len(matrix_a)  # Rows in A
    n = len(matrix_a[0])  # Cols in A (Must equal Rows in B)
    p = len(matrix_b[0])  # Cols in B

    # Initialize result matrix of size (M x P)
    result = [[0 for _ in range(p)] for _ in range(m)]

    # Triple nested loop for matrix multiplication
    for i in range(m):  # Loop through rows of A
        for j in range(p):  # Loop through columns of B
            for k in range(n):  # Loop through shared dimension N
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("        MATRIX OPERATIONS PROGRAM")
    print("=" * 60)

    # --- TESTING PART A ---
    print("\n>>> PART A: Transpose Matrix <<<")
    r_a = int(input("Enter number of rows: "))
    c_a = int(input("Enter number of columns: "))

    mat_a = get_matrix(r_a, c_a, "Original Matrix")
    display_matrix(mat_a, "Original Matrix")

    transposed_a = transpose_matrix(mat_a)
    display_matrix(transposed_a, "Transposed Matrix")

    # --- TESTING PART B ---
    print("\n>>> PART B: Matrix Addition <<<")
    print(f"Adding a second matrix of same dimensions ({r_a}x{c_a})...")
    mat_b = get_matrix(r_a, c_a, "Matrix B")

    display_matrix(mat_a, "Matrix A")
    display_matrix(mat_b, "Matrix B")

    sum_result = add_matrices(mat_a, mat_b)
    display_matrix(sum_result, "Sum Matrix (A + B)")

    # --- TESTING PART C ---
    print("\n>>> PART C: Matrix Multiplication <<<")
    print(f"For A × B, Matrix B must have {c_a} rows (matching Matrix A's columns).")
    c_b = int(input("Enter number of columns for Matrix B: "))

    mat_b_mult = get_matrix(c_a, c_b, "Matrix B for Multiplication")

    display_matrix(mat_a, "Matrix A")
    display_matrix(mat_b_mult, "Matrix B")

    product_result = multiply_matrices(mat_a, mat_b_mult)
    display_matrix(product_result, "Product Matrix (A × B)")


if __name__ == "__main__":
    main()
# =============================================================================

