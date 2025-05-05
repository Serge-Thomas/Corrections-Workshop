# employee_data.py

def read_employee_data(filename):
    names = []
    positions = []
    salaries = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                name, position, salary = line.strip().split(', ')
                names.append(name)
                positions.append(position)
                salaries.append(f"R{int(salary):,.2f}")  # Formatting salary

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return names, positions, salaries


def display_employee_data(names, positions, salaries):
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


if __name__ == "__main__":
    filename = 'employees.txt'
    names, positions, salaries = read_employee_data(filename)
    display_employee_data(names, positions, salaries)
