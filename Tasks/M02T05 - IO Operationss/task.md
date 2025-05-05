# Task - Employee Data Manager

## Auto-graded task 1: Employee Data Parser

1. Create a new Python file in the folder for this task, and call it `employee_data.py`.

2. In this Python file, write a program that reads data from the text file provided (`employees.txt`) and displays it in a structured format.

3. The `employees.txt` file contains information about employees in the following format:
   ```
   John Smith, Developer, 45000
   Sarah Johnson, Manager, 65000
   Michael Brown, Designer, 52000
   ...etc.
   ```

4. Your program should read this file and print the information in three different sections: 
   - Names
   - Positions
   - Salaries

   The output should look like:
   ```
   Names
   ---------------
   John Smith
   Sarah Johnson
   Michael Brown
   ...etc.

   Positions
   ---------------
   Developer
   Manager
   Designer
   ...etc.

   Salaries
   ---------------
   $45,000
   $65,000
   $52,000
   ...etc.
   ```

5. Make sure to format the salaries with commas as thousands separators and add dollar signs as shown above.

Before submitting your task, test your program to ensure that it correctly reads `employees.txt` and outputs the data in the required format. Remember to ensure that the text file is in the appropriate file directory or Python won't be able to find it when running your program.

## Auto-graded task 2: Inventory Manager

Follow these steps:

1. Create a file called `inventory_manager.py`.

2. Write a program that manages a store's inventory. The program should:

   - Ask the user if they want to:
     a. Add new items to inventory
     b. View current inventory
     c. Update item quantities
     d. Exit the program

3. If the user selects "Add new items":
   - Ask how many items they want to add
   - For each item, ask for:
     - Item name
     - Item price
     - Item quantity
   - Append this information to a file called `inventory.txt` in the format: `item_name,price,quantity`

4. If the user selects "View current inventory":
   - Read from the `inventory.txt` file
   - Display the information in a formatted table with columns for Item, Price, and Quantity
   - Calculate and display the total value of inventory (price × quantity for each item)

5. If the user selects "Update item quantities":
   - Display the current inventory with numbers
   - Ask the user which item number they want to update
   - Ask for the new quantity
   - Update the inventory file with the new information

6. The program should handle potential errors gracefully, such as the inventory file not existing yet or the user entering invalid input.

7. Include appropriate exception handling for file operations.

## Notes:

- Remember to use context managers (`with` statement) when dealing with files to ensure they are properly closed.
- Make sure your code is well-commented and uses descriptive variable names.
- Format your output in a way that is easy to read and understand.
- Test your program thoroughly before submission.

## Sample data for employees.txt

```
John Smith, Developer, 45000
Sarah Johnson, Manager, 65000
Michael Brown, Designer, 52000
Emily Davis, Analyst, 48000
David Wilson, Tester, 42000
```
