class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):

        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        result_kilometro = kilometers * self.fuel_consumption
        if result_kilometro <= self.fuel:
            self.fuel -= result_kilometro
