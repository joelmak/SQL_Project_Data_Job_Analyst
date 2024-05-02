class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def car_info(self):
        return(f"The speed is {self.max_speed}km & mileage is {self.mileage}km")