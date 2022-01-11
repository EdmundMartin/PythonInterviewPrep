class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.bay_counts = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.bay_counts[carType] > 0:
            self.bay_counts[carType] -= 1
            return True
        return False
