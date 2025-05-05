# Creating a travel expense calculator.
# This will ask users for their travel preference and calculate the costs.
def display_welcome():
    print("Welcome to the Travel Expense Calculator!")
    print("This will help you calculate travel costs.")
    print(
        "You can choose between a Vacation or a Road Trip Cost Calculator.\n"
    )


# This functions will be used to validate user input.
def get_valid_input(
    prompt,
    input_type=float,
    condition=lambda x: x >= 0,
    error_message="Please enter a valid number.",
):
    while True:
        try:
            value = input_type(input(prompt))
            if condition(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)


# This function will calculate the vacation budget.
def vacation_calculator():
    print("\n--- Vacation Budget Calculator ---")

    duration = get_valid_input(
        "Enter duration of the trip in days: ",
        int,
        lambda x: x > 0,
        "Duration must be a positive integer.",
    )
    accommodation_per_day = get_valid_input("Enter daily stay cost: R")
    transport_cost = get_valid_input(
        "Enter total transportation cost (e.g. flight/train): R"
    )
    food_per_day = get_valid_input("Enter your daily food budget: R")
    activities_per_day = get_valid_input("Enter your daily activities Cost: R")

    include_contingency = (
        input("Should we include contingency fund?(yes/no): ").strip().lower()
    )
    contingency_percentage = 0

    if include_contingency in ["yes", "y"]:
        contingency_percentage = get_valid_input(
            "Enter contingency percentage (10 for 10%): ",
            float,
            lambda x: x >= 0
        )

    total_accommodation = accommodation_per_day * duration
    total_food = food_per_day * duration
    total_activities = activities_per_day * duration

    subtotal = (
        total_accommodation + total_food + total_activities + transport_cost
    )
    contingency = (
        (
            subtotal * contingency_percentage / 100
            if contingency_percentage
            else 0
        )
    )
    grand_total = subtotal + contingency
    average_daily_cost = grand_total / duration

    print("\n--- Vacation Summary ---")
    print(f"Total accommodation cost: R{total_accommodation:.2f}")
    print(f"Total food cost: R{total_food:.2f}")
    print(f"Total activities cost: R{total_activities:.2f}")
    print(f"Transportation cost: R{transport_cost:.2f}")
    if contingency_percentage:
        print(f"Contingency ({contingency_percentage}%): R{contingency:.2f}")
    print(f"Grand total cost: R{grand_total:.2f}")
    print(f"Average daily cost: R{average_daily_cost:.2f}")


# This function will calculate the road trip fuel cost.
# It will ask the user for the distance, fuel efficiency and fuel price.
def road_trip_calculator():
    print("\n--- Road Trip Fuel Cost Calculator ---")

    unit = (
        input("Would you like to use (km/miles): ").strip().lower()
    )
    while unit not in ["km", "miles"]:
        print("Invalid input. Please enter 'km' or 'miles'.")
        unit = (
            input("Would you like to use kilometers or miles? (km/miles): ")
            .strip()
            .lower()
        )

    distance = get_valid_input(f"Enter the one-way trip distance in {unit}: ")
    trip_type = (
        input("Is this a one-way or round trip?): ").strip().lower()
    )
    while trip_type not in ["one-way", "round"]:
        print("Invalid input. Please enter 'one-way' or 'round'.")
        trip_type = (
            input("Is this a one-way or round trip?: ").strip().lower()
        )

    if trip_type == "round":
        total_distance = distance * 2
    else:
        total_distance = distance

    fuel_efficiency = get_valid_input(
        f"Enter your vehicle's fuel efficiency "
        f"({'km/L' if unit == 'km' else 'mpg'}): ",
        float,
        lambda x: x > 0,
    )
    fuel_price = get_valid_input(
        f"Enter the current fuel price per "
        f"{'liter' if unit == 'km' else 'gallon'}: R"
    )
    travelers = get_valid_input(
        "Enter number of travelers: ",
        int,
        lambda x: x > 0,
        "Number of travelers must be at least 1.",
    )

    fuel_needed = total_distance / fuel_efficiency
    total_fuel_cost = fuel_needed * fuel_price
    cost_per_person = total_fuel_cost / travelers

    print("\n--- Road Trip Summary ---")
    print(f"Total distance: {total_distance:.2f} {unit}")
    print(
        f"Total fuel needed: {fuel_needed:.2f} "
        f"{'liters' if unit == 'km' else 'gallons'}"
    )
    print(f"Total fuel cost: R{total_fuel_cost:.2f}")
    print(
        f"Fuel cost per person (with {travelers} traveler(s)): "
        f"R{cost_per_person:.2f}"
    )


# This function will display a welcome message.
# It will also handle invalid inputs.
def main():
    display_welcome()

    option = (
        input(
            (
                "Enter 'Vacation' to calculate a vacation budget or "
                "'Road Trip' for a fuel cost estimate: "
            )
        )
        .strip()
        .lower()
    )

    if option == "vacation":
        vacation_calculator()
    elif option == "road trip":
        road_trip_calculator()
    else:
        print(
            "\nInvalid option selected. Please restart the program and choose "
            "'Vacation' or 'Road Trip'."
        )


# This main function will run the application.
if __name__ == "__main__":
    main()
