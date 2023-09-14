#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    i = 0

    while i < len(roman_string):
        # Check for subtractive forms (e.g., IV, IX, XL, XC, etc.)
        if i + 1 < len(roman_string) and roman_string[i:i+2] in romans:
            num += romans[roman_string[i:i+2]]
            i += 2  # Move two characters forward
        else:
            num += romans[roman_string[i]]
            i += 1  # Move one character forward

    return num

