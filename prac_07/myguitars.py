from guitar import Guitar

FILENAME = "Guitars.csv"

def main():
    """Read a csv file and print a list of guitar objects."""
    guitars = read_guitars(FILENAME)

    print("Guitars read from file:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)


    name = input("Enter guitar name (or Enter to quit): ")
    while name != "":
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Enter guitar name (or Enter to quit): ")

    with open(FILENAME, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")



def read_guitars(filename):
    """Read guitars from a given file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)

main()