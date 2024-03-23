from queue import Queue
from models import Vehicle
import random

class VehicleManager:
    def __init__(self):
        self.vehicles_to_be_tested = Queue()
        self.tested_vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles_to_be_tested.put(vehicle)

    def vehicle_tested(self):
        if not self.vehicles_to_be_tested.empty():
            vehicle = self.vehicles_to_be_tested.get()
            for test in vehicle.tests:
                test.result = random.choice([True, False])
            self.tested_vehicles.append(vehicle)
            return vehicle
        return None

    def get_vehicles_to_be_tested(self):
        return list(self.vehicles_to_be_tested.queue)

    def get_tested_vehicles(self):
        return self.tested_vehicles

vehicle_manager = VehicleManager()
