#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    # Define the mapping of Roman numerals to integers
    romans = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    num = 0  # Initialize the result
    prev_value = 0  # Initialize the previous numeral value

    # Start from the end of the Roman numeral
    for char in reversed(roman_string):
        # Check if the character is a valid Roman numeral
        if char not in romans:
            return 0  # Invalid Roman numeral

        current_value = romans[char]

        # Compare the current numeral value with the previous one
        if current_value < prev_value:
            num -= current_value  # Subtract if it's smaller
        else:
            num += current_value  # Add if it's equal or larger

        prev_value = current_value  # Update the previous value

    return num

