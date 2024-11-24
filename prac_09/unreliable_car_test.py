from unreliable_car import UnreliableCar

car1 = UnreliableCar("Almost Reliable", 100, 90)
car2 = UnreliableCar("Mostly Unreliable", 100, 30)
car3 = UnreliableCar("Completely Unreliable", 100, 0)

for i in range(1, 6):
    print(f"Attempt {i}:")
    for car in [car1, car2, car3]:
        distance = car.drive(10)
        print(f"{car.name} attempted to drive 10km and actually drove {distance}km.")
    print()

