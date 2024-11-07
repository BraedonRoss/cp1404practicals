INSTRUCTIONS = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(INSTRUCTIONS)
menu_choice = input(">>> ").upper()
while menu_choice != 'Q':
    if menu_choice == 'H':
        print(f"Hello {name}")
    elif menu_choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(INSTRUCTIONS)
    menu_choice = input(">>> ").upper()
print("Finished.")
