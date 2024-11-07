import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    num_picks = int(input("How many quick picks? "))
    for i in range(num_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def generate_quick_pick():
    """Generate a single quick pick with no repeated numbers and sorted in ascending order."""
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    return quick_pick


def print_quick_pick(quick_pick):
    """Print a single quick pick with numbers aligned neatly."""
    print(" ".join(f"{number:2}" for number in quick_pick))


main()
