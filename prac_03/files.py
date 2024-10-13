# Writing the user's name to a file
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# Reading the user's name from the file and printing it
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")

# Reading the first two numbers from numbers.txt and adding them
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())

result = number1 + number2
print(result)

# Calculate the total sum of all numbers in numbers.txt
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)

print(total)

