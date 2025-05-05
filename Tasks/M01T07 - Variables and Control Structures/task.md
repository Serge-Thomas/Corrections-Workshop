# Capstone Project – Travel Expense Calculator

## Task Overview

You will create a program that helps users calculate and compare different travel expenses based on their specific needs and preferences. The program will offer two main calculation options:

1. **Vacation Budget Calculator** - Calculate total expenses for a vacation trip including accommodation, transportation, food, and activities.
2. **Road Trip Fuel Cost Calculator** - Calculate the total fuel cost for a road trip based on distance, fuel efficiency, and fuel price.

## Requirements

### Create a new Python file called `travel_calculator.py`

The program should:

1. Display a welcome message explaining the purpose of the application
2. Present the user with two options:
   - Vacation - to calculate total expenses for a vacation trip
   - Road Trip - to calculate the fuel cost for a road trip
3. Allow the user to choose an option regardless of capitalization
4. Display an appropriate error message if the user enters an invalid option

### If the user selects "Vacation":
   - Ask for the duration of the trip in days
   - Ask for the daily accommodation cost
   - Ask for the transportation cost (flight/train/bus)
   - Ask for the daily food budget
   - Ask for the daily activities budget
   - Ask if they want to include a contingency fund (yes/no)
     - If yes, ask for the contingency percentage (e.g., 10 for 10%)
   - Calculate and display:
     - Total accommodation cost
     - Total food cost
     - Total activities cost
     - Transportation cost
     - Contingency amount (if applicable)
     - Grand total for the trip
     - Average daily cost

### If the user selects "Road Trip":
   - Ask the user to choose between kilometers or miles for distance measurement
   - Ask for the total distance of the trip
   - Ask if it's a one-way trip or round trip
   - Ask for the vehicle's fuel efficiency (km/L or mpg, depending on the user's choice)
   - Ask for the current fuel price per liter or gallon
   - Calculate and display:
     - Total distance (including return journey if round trip)
     - Total fuel needed for the trip
     - Total fuel cost
     - Fuel cost per person (ask for the number of travelers)

### Formulas

#### Vacation Budget Calculator:
- Total accommodation cost = daily accommodation cost × duration
- Total food cost = daily food budget × duration
- Total activities cost = daily activities budget × duration
- Contingency amount = (accommodation + food + activities + transportation) × (contingency percentage / 100)
- Grand total = accommodation + food + activities + transportation + contingency
- Average daily cost = grand total / duration

#### Road Trip Fuel Calculator:
- Total distance = distance (× 2 if round trip)
- Total fuel needed = total distance / fuel efficiency
- Total fuel cost = total fuel needed × fuel price
- Cost per person = total fuel cost / number of travelers

### Requirements for Readability

1. Include appropriate comments to explain your code
2. Use descriptive variable names
3. Use whitespace and indentation properly
4. Ensure the output is clearly labeled and easy to read
5. Handle potential errors gracefully
