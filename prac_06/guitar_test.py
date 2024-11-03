from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
stratocaster = Guitar("Fender Stratocaster", 2013, 1300.90)

print(gibson)
print(stratocaster)

print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
print(f"{stratocaster.name} get_age() - Expected 11. Got {stratocaster.get_age()}")

print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{stratocaster.name} is_vintage() - Expected False. Got {stratocaster.is_vintage()}")
