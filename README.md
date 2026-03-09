# cp1404-2026-1-a1-Peiqiao-Xin

# CP1404 Assignment 1 – Travel Tracker 1.0

## Student Information
Name: Peiqiao Xin

Course: CP1404 Programming II  

Assignment: Assignment 1 – Travel Tracker 1.0  

Date: 8 March 2026  

GitHub Repository:https://github.com/Peiqiao-Xin/cp1404-2026-1-a1-Peiqiao-Xin.git

---

# Project Overview

Travel Tracker is a Python program designed to help users manage a list of places they want to visit. The program loads place information from a CSV file, allows the user to interact with the list through a menu-driven interface, and saves updates back to the file when the program exits.

This assignment demonstrates fundamental programming concepts taught in CP1404, including functions, file input and output, lists, exception handling, menu-based program design, and input validation.

The program allows the user to:

- View all places in the tracker
- Get a recommendation for a place to visit
- Add new places to the list
- Mark places as visited
- Save updates to the data file

---

# Program Features

The program provides several functions through a menu system.

## Display All Places

This option shows all places currently stored in the tracker. The places are sorted first by visited status (unvisited places appear first), and then by priority number. A smaller priority number represents a higher priority.

Unvisited places are marked with an asterisk `*`.

Example output:

*1. Lima in Peru 3

*2. Rome in Italy 12

3. Auckland in New Zealand 1

3 places tracked. You still want to visit 2 places.


---

## Recommend a Random Place

The program recommends a random place that has not yet been visited. This helps the user decide where to travel next.

Example:

Not sure where to visit next?
How about... Lima in Peru?


If all places have already been visited, the program will notify the user that there are no places left to visit.

---

## Add a New Place

Users can add new places to the tracker by entering the place name, country, and priority.

The program performs validation checks to ensure:

- The place name is not blank
- The country name is not blank
- The priority value is a number greater than zero

Example interaction:

Name: Tokyo

Country: Japan

Priority: 2

Tokyo in Japan (priority 2) added to Travel Tracker.


---

## Mark a Place as Visited

The user can mark a place as visited by entering the number shown in the displayed list.

The program checks that:

- The entered value is a valid number
- The number corresponds to a place in the list

Example:

Enter the number of a place to mark as visited

2

Rome in Italy visited!


If the place has already been visited, the program informs the user.

---

## Quit the Program

When the user selects `Q`, the program saves all places back to the CSV file and exits.

Example:

3 places saved to places.csv

Have a nice day :)


---

# Data File Format

The program stores travel data in a CSV file called `places.csv`.

Each line represents one place and contains four values:

Place,Country,Priority,Visited


However, the program does not include a header line. The file should contain only the data records.

Example file content:

Auckland,New Zealand,1,v

Rome,Italy,12,n

Lima,Peru,3,n


## Field Descriptions

| Field    | Description                                        |
|----------|----------------------------------------------------|
| Place    | Name of the place                                  |
| Country  | Country where the place is located                 |
| Priority | Priority number (smaller number = higher priority) |
| Visited  | `v` = visited, `n` = not visited                   |

---

# Program Structure

The program is organised using functions to improve readability and maintainability.

## Main Function

The `main()` function controls the overall program flow. It loads the places from the CSV file, displays the menu repeatedly, processes user input, and saves the data when the program exits.

## File Handling Functions

`load_places()`  
Reads the CSV file and loads the data into a list of places.

`save_places()`  
Writes the updated list of places back to the CSV file.

## Display and Processing Functions

`display_places()`  
Displays all places sorted by visited status and priority.

`recommend_place()`  
Selects a random unvisited place and recommends it to the user.

`add_place()`  
Prompts the user to enter a new place and adds it to the list.

`mark_place_visited()`  
Marks a selected place as visited.

## Validation Functions

To improve code reuse and reliability, several validation functions are used:

- `get_non_blank_string()` ensures text input is not empty.
- `get_positive_number()` ensures numeric input is greater than zero.
- `get_valid_place_number()` ensures the selected place number exists.

These functions help keep the code organised and reduce repetition.

---

# Programming Techniques Used

Several programming practices were applied when developing this program.

## Constants

Constants are used to represent fixed values such as the visited status and the data file name.

VISITED = "v"

UNVISITED = "n"

FILENAME = "places.csv"


Using constants improves readability and avoids repeating literal values throughout the program.

## Exception Handling

The program uses `try` and `except` blocks to safely handle invalid user input.

Examples include:

- `ValueError` for invalid numeric input
- `IndexError` for invalid place numbers

This prevents the program from crashing when users enter incorrect input.

## Menu Pattern

The program uses a loop to repeatedly display the menu until the user chooses to quit.

while menu_choice != "Q"


This pattern allows the user to continue interacting with the program until they decide to exit.

## Sorting

Places are sorted using a custom key function so that:

1. Unvisited places appear first
2. Lower priority numbers appear before higher ones

This ensures that the most important unvisited places appear at the top of the list.

---

# Lessons Learned

During this assignment, I improved my understanding of several programming concepts, including file input and output, list manipulation, and function design.

I also learned how to structure a program using reusable functions, implement input validation, and use exception handling to make the program more robust.

Working on this project also helped me practice writing clearer documentation and organising code in a way that is easier to read and maintain.

---

# References

CP1404 Programming II lecture materials  

Assignment 1 specification – Travel Tracker 1.0