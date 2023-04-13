class ParkingSystem:
    # T : O(1), S : O(1)
    def __init__(self, big: int, medium: int, small: int):
        self.capacity = [big, medium, small]

    # T : O(1), S : O(1)
    def addCar(self, carType: int) -> bool:
        if self.capacity[carType - 1] > 0:
            self.capacity[carType - 1] -= 1
            return True
        return False


if __name__ == "__main__":
    ps = ParkingSystem(big=1, medium=1, small=0)
    assert ps.addCar(1)
    assert ps.addCar(2)
    assert not ps.addCar(3)
    assert not ps.addCar(2)
    assert not ps.addCar(1)
