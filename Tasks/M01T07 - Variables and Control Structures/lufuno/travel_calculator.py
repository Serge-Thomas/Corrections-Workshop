# travel_calculator.py


def welcome_message():
    """Display a welcome message explaining the purpose of the application."""
    print("Welcome to the South Africa Travel Expense Calculator!")
    print(
        "This program helps you calculate and compare different travel\
expenses based on your needs and preferences within South Africa.\n"
    )


def vacation_budget_calculator():
    """Calculate total expenses for a vacation trip."""
    try:
        # Get user input for vacation details
        duration = int(input("Enter the duration of your trip in days: "))
        if duration <= 0:
            print("Duration must be a positive integer.")
            return

        daily_accommodation_cost = float(
            input("Enter the daily accommodation cost (in ZAR): R")
        )
        if daily_accommodation_cost < 0:
            print("Cost cannot be negative.")
            return

        transportation_cost = float(
            input("Enter the transportation cost (flight/train/bus) (in ZAR)\
: R")
        )
        if transportation_cost < 0:
            print("Cost cannot be negative.")
            return

        daily_food_budget = float(input("Enter your daily food budget (in ZAR)\
: R"))
        if daily_food_budget < 0:
            print("Cost cannot be negative.")
            return

        daily_activities_budget = float(
            input("Enter your daily activities budget (in ZAR): R")
        )
        if daily_activities_budget < 0:
            print("Cost cannot be negative.")
            return

        # Ask if they want to include a contingency fund
        include_contingency = (
            input("Do you want to include a contingency fund? (yes/no): ")
            .strip()
            .lower()
        )
        contingency_amount = 0

        if include_contingency == "yes":
            contingency_percentage = float(
                input("Enter the contingency percentage (e.g., 10 for 10%): ")
            )
            if contingency_percentage < 0:
                print("Contingency percentage cannot be negative.")
                return
            # Calculate contingency amount
            total_expenses_before_contingency = (
                daily_accommodation_cost * duration
                + transportation_cost
                + daily_food_budget * duration
                + daily_activities_budget * duration
            )
            contingency_amount = total_expenses_before_contingency * (
                contingency_percentage / 100
            )
        elif include_contingency != "no":
            print("Invalid input for contingency fund. Please enter 'yes' or \
'no'.")
            return

        # Calculate total costs
        total_accommodation_cost = daily_accommodation_cost * duration
        total_food_cost = daily_food_budget * duration
        total_activities_cost = daily_activities_budget * duration
        grand_total = (
            total_accommodation_cost
            + total_food_cost
            + total_activities_cost
            + transportation_cost
            + contingency_amount
        )
        average_daily_cost = grand_total / duration

        # Display results
        print("\n--- Vacation Budget Summary ---")
        print(f"Total accommodation cost: R{total_accommodation_cost:.2f}")
        print(f"Total food cost: R{total_food_cost:.2f}")
        print(f"Total activities cost: R{total_activities_cost:.2f}")
        print(f"Transportation cost: R{transportation_cost:.2f}")
        print(f"Contingency amount: R{contingency_amount:.2f}")
        print(f"Grand total for the trip: R{grand_total:.2f}")
        print(f"Average daily cost: R{average_daily_cost:.2f}\n")
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")


def road_trip_fuel_calculator():
    """Calculate the total fuel cost for a road trip."""
    try:
        # Get user input for road trip details
        # Defaulting to kilometers/liters as South Africa uses metric system
        distance_unit = (
            input(
                "Choose distance measurement (kilometers/miles) [default: \
kilometers]: "
            )
            .strip()
            .lower()
        )
        if distance_unit == "":
            distance_unit = "kilometers"
        if distance_unit not in ["kilometers", "miles"]:
            print("Invalid distance measurement. Please enter 'kilometers' or\
 'miles'.")
            return

        total_distance = float(
            input(f"Enter the total distance of the trip in {distance_unit}: ")
        )
        if total_distance <= 0:
            print("Distance must be a positive number.")
            return

        trip_type = (
            input("Is it a one-way trip or round trip? (one-way/round): ")
            .strip()
            .lower()
        )
        if trip_type not in ["one-way", "round"]:
            print("Invalid trip type. Please enter 'one-way' or 'round'.")
            return

        if trip_type == "round":
            total_distance *= 2  # Double the distance for round trip

        fuel_efficiency = float(
            input("Enter the vehicle's fuel efficiency (km/L or mpg): ")
        )
        if fuel_efficiency <= 0:
            print("Fuel efficiency must be a positive number.")
            return

        unit_label = "liter" if distance_unit == "kilometers" else "gallon"
        fuel_price = float(
            input(f"Enter the current fuel price per {unit_label} (in ZAR): R")
        )
        if fuel_price < 0:
            print("Fuel price cannot be negative.")
            return

        # Calculate total fuel needed and cost
        total_fuel_needed = total_distance / fuel_efficiency
        total_fuel_cost = total_fuel_needed * fuel_price

        # Get number of travelers for cost per person
        number_of_travelers = int(input("Enter the number of travelers: "))
        if number_of_travelers <= 0:
            print("Number of travelers must be a positive integer.")
            return

        cost_per_person = total_fuel_cost / number_of_travelers

        # Display results
        print("\n--- Road Trip Fuel Cost Summary ---")
        print(f"Total distance: {total_distance:.2f} {distance_unit}")
        print(f"Total fuel needed: {total_fuel_needed:.2f} {unit_label}s")
        print(f"Total fuel cost: R{total_fuel_cost:.2f}")
        print(f"Fuel cost per person: R{cost_per_person:.2f}\n")
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")


def main():
    """Main function to run the travel calculator."""
    welcome_message()

    while True:
        # Present options to the user
        option = input("Choose an option \
(Vacation/Road Trip): ").strip().lower()

        if option == "vacation":
            vacation_budget_calculator()
        elif option == "road trip":
            road_trip_fuel_calculator()
        else:
            print("Invalid option. Please enter 'Vacation' or 'Road Trip'.")
            continue

        # Ask if the user wants to perform another calculation
        another = (
            input("Would you like to perform another calculation? (yes/no): ")
            .strip()
            .lower()
        )
        if another != "yes":
            print(
                "Thank you for using the South Africa Travel Expense \
Calculator. Safe travels!"
            )
            break


main()
