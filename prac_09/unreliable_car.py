import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Represent an Unreliable Car object."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0