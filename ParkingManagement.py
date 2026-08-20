class ParkingManagement:

    def __init__(self):
        self.slots = {
            "Bike": ["B1", "B2"],
            "Car": ["C1", "C2"],
            "SUV": ["S1"],
            "Truck": ["T1"],
            "EV": ["E1"]
        }

        self.parked = {}
        self.ticket = 1

        self.fee = {
            "Bike": 20,
            "Car": 50,
            "SUV": 70,
            "Truck": 100,
            "EV": 60
        }

    # Vehicle Entry
    def entry(self, vehicle, vtype, vip=False):

        if vehicle in self.parked:
            return "Duplicate Vehicle"

        if vtype not in self.slots:
            return "Invalid Vehicle"

        available = self.slots[vtype]

        if not available:
            return "Parking Full"

        slot = available.pop(0)

        t = "T" + str(self.ticket)
        self.ticket += 1

        self.parked[vehicle] = {
            "type": vtype,
            "slot": slot,
            "ticket": t,
            "vip": vip
        }

        return {
            "ticket": t,
            "slot": slot,
            "status": "Parked"
        }

    # Vehicle Exit
    def exit(self, vehicle, hours, lost=False, peak=False):

        if vehicle not in self.parked:
            return "Invalid Vehicle"

        data = self.parked[vehicle]

        if lost:
            fee = 500
        else:
            fee = self.fee[data["type"]] * max(1, hours)

        # Peak hour pricing
        if peak and not lost:
            fee *= 1.5

        # VIP gets 20% discount
        if data["vip"] and not lost:
            fee *= 0.8

        # EV charging
        if data["type"] == "EV" and not lost:
            fee += 100

        # Return slot
        self.slots[data["type"]].append(data["slot"])

        del self.parked[vehicle]

        return round(fee, 2)
