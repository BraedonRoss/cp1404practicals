"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint

def main():
    user_score = float(input("Enter score: "))
    user_result = determine_result(user_score)
    print(user_result)
    random_score = randint(1,100)
    random_result = determine_result(random_score)
    print(random_result)



def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    if score <= 100:
        return "Excellent"



main()
