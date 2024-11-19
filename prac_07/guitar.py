'''
Estimated Time: 20 mins
Actual Time:  25 mins

'''
YEAR = 2024


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        return YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50
