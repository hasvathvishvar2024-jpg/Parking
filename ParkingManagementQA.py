from ParkingManagement import ParkingManagement
passed = 0
def test(no, name, expected, actual):
    global passed
    status = "PASS" if expected == actual else "FAIL"
    print("TC", no, "-", name)
    print("Expected:", expected)
    print("Actual:", actual)
    print("Status:", status)
    print()
    if status == "PASS":
        passed += 1
p = ParkingManagement()
p.entry("B1", "Bike")
p.entry("B2", "Bike")
r = p.entry("B3", "Bike")
test(
    1,
    "Full Parking Lot",
    "Parking Full",
    r
)
p = ParkingManagement()
r = p.entry("CAR1", "Truck")
test(
    2,
    "Wrong Vehicle-Slot Combination",
    "Parking Full",
    r
)
p = ParkingManagement()
p.entry("CAR1", "Car")
r = p.entry("CAR1", "Car")
test(
    3,
    "Duplicate Vehicle",
    "Duplicate Vehicle",
    r
)
p = ParkingManagement()
p.entry("CAR1", "Car")
r = p.exit(
    "CAR1",
    2,
    lost=True
)
test(
    4,
    "Lost Ticket",
    500,
    r
)
p = ParkingManagement()
p.entry("CAR1", "Car")
r = p.exit(
    "CAR1",
    0
)
test(
    5,
    "Early Exit",
    50,
    r
)
p = ParkingManagement()
p.entry("TRUCK1", "Truck")
r = p.exit(
    "TRUCK1",
    12
)
test(
    6,
    "Overnight Parking",
    1200,
    r
)
p = ParkingManagement()
p.entry("CAR1", "Car")
r = p.exit(
    "CAR1",
    2,
    peak=True
)
test(
    7,
    "Peak Hour Pricing",
    150,
    r
)
p = ParkingManagement()
p.entry("EV1", "EV")
r = p.exit(
    "EV1",
    2
)
test(
    8,
    "EV Charging Fee",
    220,
    r
)
print("======================")
print("TOTAL TESTS:", 8)
print("PASSED:", passed)
print("FAILED:", 8 - passed)
print("======================")
