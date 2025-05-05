# This script reads employee data from a file and print in a formatted way.
# The file should contain lines in the format: Name, Position, Salary
def read_employee_data(filename):
    names = []
    positions = []
    salaries = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                if len(parts) == 3:
                    name, position, salary = parts
                    names.append(name)
                    positions.append(position)
                    # Convert salary to int and store formatted version
                    try:
                        salary_int = int(salary)
                        formatted_salary = f"${salary_int:,.0f}"
                        salaries.append(formatted_salary)
                    except ValueError:
                        salaries.append("Invalid Salary")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    # Print output
    print("Names")
    print("---------------")
    for name in names:
        print(name)

    print("\nPositions")
    print("---------------")
    for position in positions:
        print(position)

    print("\nSalaries")
    print("---------------")
    for salary in salaries:
        print(salary)


# Replace 'employees.txt' with the actual path if it's in a different folder.
if __name__ == "__main__":
    read_employee_data('employees.txt')
