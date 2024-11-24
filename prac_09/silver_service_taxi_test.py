from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 2)

hummer.start_fare()
hummer.drive(18)
fare = hummer.get_fare()
print(hummer)
print(f"Fare for 18 km trip: ${fare:.2f}")

assert round(fare, 2) == 48.78, f"Expected fare to be $48.78 but got ${fare:.2f}"
