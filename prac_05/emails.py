"""
Emails
Estimate: 20 minutes
Actual:   13 minutes
"""

def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)

        correct = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if correct != "" and correct != "y":
            name = input("Name: ")
        email_to_name[email] = name

        email = input("Email: ")

    print("\nStored emails and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()