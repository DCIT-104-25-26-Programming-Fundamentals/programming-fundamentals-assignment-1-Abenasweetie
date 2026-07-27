# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================

# -----------------------------------------------------------------------------
# FEATURE FUNCTIONS
# -----------------------------------------------------------------------------
def add_task(tasks):
    """
    Prompts the user for a task description and adds it to the list.
    """
    task_desc = input("Enter task: ").strip()

    if not task_desc:
        print("Error: Task description cannot be empty.")
        return

    tasks.append(task_desc)
    print(f'Task added: "{task_desc}"')


def view_tasks(tasks):
    """
    Displays all tasks currently in the list with 1-based numbering.
    """
    if not tasks:
        print("Your task list is currently empty!")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"  {index}. {task}")


def delete_task(tasks):
    """
    Displays the current list and removes a task chosen by the user.
    """
    if not tasks:
        print("Your list is empty. There are no tasks to delete.")
        return

    # First, display current tasks so the user knows the numbers
    view_tasks(tasks)

    try:
        task_num = int(input("\nEnter task number to delete: "))

        # Check if the entered number corresponds to a valid 1-based index
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f'Task "{removed}" has been removed.')
        else:
            print("Error: Invalid task number. Please select a number from the list.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")


def display_menu():
    """
    Prints the interactive main menu options.
    """
    print("\n" + "=" * 28)
    print("       TO-DO LIST MENU")
    print("=" * 28)
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


# -----------------------------------------------------------------------------
# MAIN PROGRAM LOOP
# -----------------------------------------------------------------------------
def main():
    # Store all tasks in a dynamic Python list
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Error: Invalid option. Please enter a choice between 1 and 4.")


if __name__ == "__main__":
    main()
# =============================================================================

