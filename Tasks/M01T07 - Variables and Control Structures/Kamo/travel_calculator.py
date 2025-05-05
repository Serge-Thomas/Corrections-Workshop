# Defining welcome message

def welcome_message():
    print("Welcome to the Travel Savings calculator!")
    print("This program will help you to calculate the total cost for vacation or a road trip.\n")


#  Defining user choice
def user_choice():
    print("Please choose an option:")
    print("1. Vacation - Calculate total cost for a vacation trip")
    print("2. Road Trip - Calculate the fuel cost for a road trip")
    return input("Enter 'Vacation' or 'Road Trip': ").strip().lower()


# Defining vacation_calculator
def vacation_calculator():
    try:
        duration = int(input("Enter the duration of your trip in days: "))
        daily_accommodation = float(input("Enter the daily accommodation cost: "))
        transportation = float(input("Enter the transportation cost (flight/train/bus): "))
        daily_food = float(input("Enter your daily food budget: "))
        daily_activities = float(input("Enter your daily activities budget: "))
        include_contingency = input("Do you want to include a contingency fund? (yes/no): ").strip().lower()

        # Calculate base costs
        total_accommodation = daily_accommodation * duration
        total_food = daily_food * duration
        total_activities = daily_activities * duration
        base_total = total_accommodation + total_food + total_activities + transportation

        contingency_amount = 0
        if include_contingency == "yes":
            contingency_percent = float(input("Enter contingency percentage (e.g., 10 for 10%): "))
            contingency_amount = base_total * (contingency_percent / 100)

        grand_total = base_total + contingency_amount
        average_daily_cost = grand_total / duration

        # printing the results
        print("\nVacation Budget Summary:")
        print(f"Total accommodation cost: R{total_accommodation:.2f}")
        print(f"Total food cost: R{total_food:.2f}")
        print(f"Total activities cost: R{total_activities:.2f}")
        print(f"Transportation cost: R{transportation:.2f}")
        if contingency_amount:
            print(f"Contingency amount: R{contingency_amount:.2f}")
        print(f"Grand total for the trip: R{grand_total:.2f}")
        print(f"Average daily cost: R{average_daily_cost:.2f}")

    except ValueError:
        print("Error: Please enter valid numeric values.")

#  Defining road trip.


def road_trip_calculator():
    try:
        unit = input("Would you like to use kilometers or miles? (km/miles): ").strip().lower()
        if unit not in ["km", "miles"]:
            print("Invalid unit. Please enter 'km' or 'miles'.")
            return

        distance = float(input("Enter the total distance of the trip: "))
        trip_type = input("Is this a one-way or round trip? (one-way/round): ").strip().lower()
        fuel_efficiency = float(input(f"Enter the vehicle's fuel efficiency ({'km/L' if unit == 'km' else 'mpg'}): "))
        fuel_price = float(input(f"Enter the current fuel price per {'liter' if unit == 'km' else 'gallon'}: "))
        travelers = int(input("Enter the number of travelers: "))

        if trip_type == "round":
            distance *= 2

        total_fuel_needed = distance / fuel_efficiency
        total_fuel_cost = total_fuel_needed * fuel_price
        cost_per_person = total_fuel_cost / travelers

        # Displaying the results
        print("\nRoad Trip Fuel Cost Summary:")
        print(f"Total distance: R{distance:.2f} {unit}")
        print(f"Total fuel needed: R{total_fuel_needed:.2f} {'liters' if unit == 'km' else 'gallons'}")
        print(f"Total fuel cost: R{total_fuel_cost:.2f}")
        print(f"Fuel cost per person: R{cost_per_person:.2f}")

    except ValueError:
        print("Error: Please enter valid numeric values.")

# Defining main.


def main():
    welcome_message()
    choice = user_choice()

    if choice == "vacation":
        vacation_calculator()
    elif choice == "road trip":
        road_trip_calculator()
    else:
        print("Invalid option. Please restart the program and choose 'Vacation' or 'Road Trip'.")


if __name__ == "__main__":
    main()
