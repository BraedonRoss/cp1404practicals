MENU = '(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit'


def main():
    score = 0
    print(MENU)
    menu_choice = input("Choice: ").upper()
    while menu_choice != 'Q':
        if menu_choice == 'G':
            score = get_valid_score()
        elif menu_choice == 'P':
            result = determine_result(score)
            print(result)
        elif menu_choice == 'S':
            print(score * '*')
        else:
            print("Invalid Menu Choice")
        print(MENU)
        menu_choice = input("Choice: ").upper()


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score

def determine_result(score):
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    if score <= 100:
        return "Excellent"

main()



