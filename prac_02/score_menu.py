MENU = '(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit'

print(MENU)
menu_choice = input("Choice: ").upper()
while menu_choice != 'Q':
    if menu_choice == 'G':
        pass
    elif menu_choice == 'P':
        pass
    elif menu_choice == 'S':
        pass
    else:
        print("Invalid Menu Choice")
    print(MENU)
    menu_choice = input("Choice: ").upper()



