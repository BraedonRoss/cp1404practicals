from guitar import Guitar

def main():
    print("my guitars!")
    guitars = []
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} Added.")
        name = input("\nName: ")

    print_guitar_statement(guitars)


def print_guitar_statement(guitars):
    print("These Are My Guitars:")
    for i,guitar in enumerate(guitars, start=1):
        vintage_string = "(Vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()