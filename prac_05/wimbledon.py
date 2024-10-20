FILENAME = "Wimbledon_data.csv"

def main():
    pass

def read_csv_data(filename):
    """Read the Wimbledon CSV file and return the data as a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            row = line.strip().split(',')
            data.append(row)
    return data

