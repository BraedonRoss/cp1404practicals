from guitar import Guitar

FILENAME = "Guitars.csv"

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