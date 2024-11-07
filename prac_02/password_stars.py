def main():
    MIN_LENGTH = 6
    user_password = get_password(MIN_LENGTH)
    print_as_asterisks(user_password)


def print_as_asterisks(user_password):
    print("*" * len(user_password))


def get_password(MIN_LENGTH):
    user_password = input("Please type your password: ")
    while len(user_password) < MIN_LENGTH:
        print("Invalid Pass: too short")
        user_password = input("Please type your password: ")
    return user_password


main()
