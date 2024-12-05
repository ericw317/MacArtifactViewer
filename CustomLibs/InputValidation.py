import os

# input validation for an integer between two numbers
def int_between_numbers(prompt, lower_num, upper_num):
    while True:
        try:
            number = int(input(prompt))  # prompt the user

            # run input validation
            if lower_num <= number <= upper_num:
                return number  # return number once it passes input validation
            else:
                print(f"Error: Input must be an integer between {lower_num} and {upper_num}")
        except ValueError:
            print("Error: Input must be an integer.")

# file path exists
def file_path(prompt):
    while True:
        path = input(prompt)
        if os.path.exists(path) or path == "-1":
            return path
        else:
            print(f"Error: Path not found. Try again.\n")

# string match
def string_match(prompt, string_list):
    while True:
        string = input(prompt)

        if string in string_list:
            return string
        else:
            print("Error: Invalid Input.")

# yes or no
def yes_or_no(prompt):
    while True:
        response = (input(prompt)).lower()

        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Error: Invalid input.")