"""
Emails
Estimate: 20 minutes
Actual:   13 minutes
"""

def main():
    """Extract a name from an inputted email and print a list of names and associated emails."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)

        correct_name = input(f"Is your name {name}? (Y/n) ").lower()
        if correct_name != "" and correct_name != "y":
            name = input("Name: ")
        email_to_name[email] = name

        email = input("Email: ")


    print("\nStored emails and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Extract a name from the provided email."""
    first_half_email = email.split('@')[0]
    name_parts = first_half_email.split('.')
    name = " ".join(name_parts).title()
    return name

main()