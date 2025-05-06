def get_employee_details(file_path):
    try:
        with open(file_path, 'r') as f:
            raw_lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return [], [], []

    staff = []
    roles = []
    incomes = []

    for line in raw_lines:
        parts = line.strip().split(',')
        if len(parts) == 3:
            full_name = parts[0].strip()
            job = parts[1].strip()
            try:
                earnings = int(parts[2].strip())
            except ValueError:
                print(f"Skipped invalid salary for {full_name}")
                continue

            staff.append(full_name)
            roles.append(job)
            incomes.append(earnings)
        else:
            print(f"Skipped improperly formatted line: {line.strip()}")

    return staff, roles, incomes


def print_section(title, items, is_money=False):
    print(f"{title}")
    print("=" * len(title))
    for item in items:
        if is_money:
            print(f"R{item:,.0f}")
        else:
            print(item)
    print()


def main():
    file_name = "employees.txt"
    names, jobs, salaries = get_employee_details(file_name)

    print_section("Employee Names", names)
    print_section("Job Titles", jobs)
    print_section("Monthly Salaries (ZAR)", salaries, is_money=True)


main()
