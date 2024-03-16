from queue import Queue
from models import Vehicle
import random

class VehicleManager:
    def __init__(self):
        self.vehicles_to_be_tested = Queue()
        self.tested_vehicles = []
        self.vehicle_lookup = {}

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles_to_be_tested.put(vehicle)
        self.vehicle_lookup[vehicle.tuition] = vehicle

    def vehicle_tested(self, tuition: str):
        vehicle = self.vehicle_lookup.get(tuition)
        if vehicle:
            del self.vehicle_lookup[tuition]
            self.tested_vehicles.append(vehicle)

    def get_vehicles_to_be_tested(self):
        return list(self.vehicles_to_be_tested.queue)

    def get_tested_vehicles(self):
        return self.tested_vehicles
    
    def execute_tests_for_vehicle(self):
        if not self.vehicles_to_be_tested.empty():
            vehicle = self.vehicles_to_be_tested.get()
            del self.vehicle_lookup[vehicle.tuition]
            for test in vehicle.tests:
                test.result = random.choice([True, False])
            self.tested_vehicles.append(vehicle)
            return vehicle
        return None
    
    def remove_pending_vehicle(self, tuition: str):
        vehicle = self.vehicle_lookup.get(tuition)
        if vehicle:
            del self.vehicle_lookup[tuition]
            return True
        return False

vehicle_manager = VehicleManager()