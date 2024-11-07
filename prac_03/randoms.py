import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""Questions"""

# 1.    5 was the smallest possible number, 20 was the largest
#
# 2.    3 was the smallest possible number, 9 was the largest
#       line 2 could not have produced a 4
#
# 3.    2.5 is the smallest possible number, 5.5 was the largest

print(random.randint(1, 100))
