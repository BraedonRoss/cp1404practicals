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

def process_countries(data):
    """Process the data to extract unique countries of champions."""
    countries = set()
    for row in data:
        country = row[2]
        countries.add(country)
    return sorted(countries)

def process_champions(data):
    """Process the data to count the win counts for each champion."""
    champions_count = {}
    for row in data:
        champion = row[1]
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1
    return champions_count

