# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def calculate_average(scores):
    """
    Helper function to calculate the average of a list of numeric scores.
    Returns 0.0 if the list is empty.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# -----------------------------------------------------------------------------
# FEATURE FUNCTIONS
# -----------------------------------------------------------------------------
def add_student(students):
    """
    Prompts the user for student details (Name, ID, Scores) and appends
    a new dictionary record to the students list.
    """
    print("\n--- Add New Student ---")
    name = input("Student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    # ID validation
    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Student ID must be an integer.")
        return

    # Check for duplicate student ID
    for s in students:
        if s["id"] == student_id:
            print(f"Error: A student with ID {student_id} already exists.")
            return

    # Score input loop
    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Error: Number of scores must be greater than 0.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    scores = []
    for i in range(1, num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("  -> Error: Score should be between 0 and 100.")
            except ValueError:
                print("  -> Error: Please enter a valid numerical score.")

    # Create record and append to database list
    student_record = {"name": name, "id": student_id, "scores": scores}

    students.append(student_record)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """
    Prints a neatly aligned table displaying every student's Name, ID,
    individual scores, and overall calculated average.
    """
    if not students:
        print("\nNo student records found.")
        return

    header = f"{'Name':<20} {'ID':<12} {'Scores':<20} {'Average':<8}"
    line = "-" * len(header)

    print("\n" + line)
    print(header)
    print(line)

    for student in students:
        name = student["name"]
        sid = str(student["id"])
        # Format scores as a comma-separated string (displaying integers cleanly)
        scores_str = ", ".join(
            f"{s:.0f}" if s.is_integer() else f"{s:.1f}"
            for s in student["scores"]
        )
        avg = calculate_average(student["scores"])

        print(f"{name:<20} {sid:<12} {scores_str:<20} {avg:<8.2f}")

    print(line)


def calculate_student_average(students):
    """
    Finds a specific student by their ID and displays their calculated average score.
    """
    if not students:
        print("\nNo student records found.")
        return

    try:
        target_id = int(input("\nEnter student ID: "))
    except ValueError:
        print("Error: Invalid ID format. Must be an integer.")
        return

    # Search for matching student
    for student in students:
        if student["id"] == target_id:
            avg = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {avg:.2f}")
            return

    # If the loop finishes without returning, the student was not found
    print(f"Error: Student with ID {target_id} not found.")


def display_menu():
    """
    Prints the interactive menu choices.
    """
    print("\n" + "=" * 32)
    print("   STUDENT RECORD SYSTEM MENU")
    print("=" * 32)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


# -----------------------------------------------------------------------------
# MAIN PROGRAM LOOP
# -----------------------------------------------------------------------------
def main():
    # Primary data structure storing all student dictionaries
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Error: Invalid option. Please enter a choice between 1 and 4.")


if __name__ == "__main__":
    main()
# =============================================================================

