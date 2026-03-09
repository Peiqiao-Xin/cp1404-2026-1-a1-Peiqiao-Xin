"""
CP1404/CP5632 Assignment 1 - Travel Tracker 1.0

Name: Peiqiao Xin
Date: 08/03/2026
GitHub repository:https://github.com/Peiqiao-Xin/cp1404-2026-1-a1-Peiqiao-Xin.git

Travel Tracker program that loads places from a CSV file, allows the user to
display places, recommend a random unvisited place, add a new place, mark a
place as visited, and save the updated data when quitting.
"""

import random

VISITED = "v"
UNVISITED = "n"
FILENAME = "place.csv"


def main():
    """Run the Travel Tracker program."""
    print("Travel Tracker 1.0 - by Your Name")
    places = load_places(FILENAME)
    print(f"{len(places)} places loaded from {FILENAME}")

    menu_choice = ""
    while menu_choice != "Q":
        print_menu()
        menu_choice = input(">>> ").strip().upper()

        if menu_choice == "D":
            display_places(places)
        elif menu_choice == "R":
            recommend_place(places)
        elif menu_choice == "A":
            add_place(places)
        elif menu_choice == "M":
            mark_place_visited(places)
        elif menu_choice == "Q":
            save_places(FILENAME, places)
            print(f"{len(places)} places saved to {FILENAME}")
            print("Have a nice day :)")
        else:
            print("Invalid menu choice")


def print_menu():
    """Display the program menu."""
    print("Menu:")
    print("D - Display all places")
    print("R - Recommend a random place")
    print("A - Add a new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def load_places(filename):
    """Load places from filename into a list of lists."""
    places = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            name = parts[0]
            country = parts[1]
            priority = int(parts[2])
            visited_status = parts[3]
            places.append([name, country, priority, visited_status])
    return places


def save_places(filename, places):
    """Save places to filename in CSV format."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for place in places:
            out_file.write(f"{place[0]},{place[1]},{place[2]},{place[3]}\n")


def display_places(places):
    """Display all places sorted by visited status then priority."""
    places.sort(key=place_sort_key)

    max_name_width = get_maximum_name_width(places)
    max_country_width = get_maximum_country_width(places)

    unvisited_count = 0
    for index, place in enumerate(places, start=1):
        marker = "*" if place[3] == UNVISITED else ""
        if place[3] == UNVISITED:
            unvisited_count += 1
        print(
            f"{marker}{index}. "
            f"{place[0]:<{max_name_width}} in "
            f"{place[1]:<{max_country_width}} "
            f"{place[2]}"
        )

    print(f"{len(places)} places tracked. You still want to visit {unvisited_count} places.")


def place_sort_key(place):
    """Return the sort key for a place."""
    return place[3], place[2]


def get_maximum_name_width(places):
    """Return the width of the longest place name."""
    maximum_width = 0
    for place in places:
        if len(place[0]) > maximum_width:
            maximum_width = len(place[0])
    return maximum_width


def get_maximum_country_width(places):
    """Return the width of the longest country name."""
    maximum_width = 0
    for place in places:
        if len(place[1]) > maximum_width:
            maximum_width = len(place[1])
    return maximum_width


def recommend_place(places):
    """Recommend a random unvisited place."""
    unvisited_places = get_unvisited_places(places)

    if len(unvisited_places) == 0:
        print("No places left to visit!")
    else:
        random_place = random.choice(unvisited_places)
        print("Not sure where to visit next?")
        print(f"How about... {random_place[0]} in {random_place[1]}?")


def get_unvisited_places(places):
    """Return a list of unvisited places."""
    unvisited_places = []
    for place in places:
        if place[3] == UNVISITED:
            unvisited_places.append(place)
    return unvisited_places


def add_place(places):
    """Prompt for a new place and add it to the list."""
    name = get_non_blank_string("Name: ")
    country = get_non_blank_string("Country: ")
    priority = get_positive_number("Priority: ")

    new_place = [name, country, priority, UNVISITED]
    places.append(new_place)
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def mark_place_visited(places):
    """Mark a selected place as visited if possible."""
    if count_unvisited_places(places) == 0:
        print("No unvisited places")
        return

    display_places(places)
    print("Enter the number of a place to mark as visited")

    place_number = get_valid_place_number(places)
    selected_place = places[place_number - 1]

    if selected_place[3] == VISITED:
        print(f"You have already visited {selected_place[0]}")
    else:
        selected_place[3] = VISITED
        print(f"{selected_place[0]} in {selected_place[1]} visited!")


def count_unvisited_places(places):
    """Count and return the number of unvisited places."""
    unvisited_count = 0
    for place in places:
        if place[3] == UNVISITED:
            unvisited_count += 1
    return unvisited_count


def get_non_blank_string(prompt):
    """Prompt for a non-blank string and return it."""
    user_input = input(prompt).strip()
    while user_input == "":
        print("Input can not be blank")
        user_input = input(prompt).strip()
    return user_input


def get_positive_number(prompt):
    """Prompt for a positive integer greater than 0 and return it."""
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be > 0")
            else:
                return number
        except ValueError:
            print("Invalid input; enter a valid number")


def get_valid_place_number(places):
    """Prompt for a valid place number and return it."""
    while True:
        try:
            place_number = int(input(">>> "))
            if place_number <= 0:
                print("Number must be > 0")
            else:
                try:
                    places[place_number - 1]
                    return place_number
                except IndexError:
                    print("Invalid place number")
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == "__main__":
    main()