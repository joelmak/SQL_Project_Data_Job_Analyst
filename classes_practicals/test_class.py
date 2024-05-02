import unittest
from classes import Vehicle

class TestVehicle(unittest.TestCase):
    def test_vehicle_info(self):
        car = Vehicle(100,5000)
        self.assertEqual(car.car_info(),"The speed is 100km & mileage is 5000km")

if __name__ =='__main__':
    unittest.main()


