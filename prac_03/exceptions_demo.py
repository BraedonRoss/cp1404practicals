"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Please enter a valid denominator.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1.    A ValueError will occur if the user enters a non integer value such as a float or a string
# 2.    A ZeroDivisionError will occur if the user inputs 0 as the denominator
# 3.    Yes, you can change the code to check if the denominator is zero before performing the division.