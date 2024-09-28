MIN_LENGTH = 6
user_password = input("Please type your password: ")
while len(user_password) < MIN_LENGTH:
    print("Invalid Pass: too short")
    user_password = input("Please type your password: ")
print("*" * len(user_password))
