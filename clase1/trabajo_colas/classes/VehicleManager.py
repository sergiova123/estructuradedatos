from collections import deque
from models import Vehicle
import random

class VehicleManager:
    def __init__(self):
        self.vehicles_to_be_tested = deque()
        self.tested_vehicles = []
        self.vehicle_lookup = {}

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles_to_be_tested.append(vehicle)
        self.vehicle_lookup[vehicle.tuition] = vehicle

    def vehicle_tested(self, tuition: str):
        vehicle = self.vehicle_lookup.get(tuition)
        if vehicle:
            self.vehicles_to_be_tested.remove(vehicle)
            self.tested_vehicles.append(vehicle)
            del self.vehicle_lookup[tuition]

    def get_vehicles_to_be_tested(self):
        return list(self.vehicles_to_be_tested)

    def get_tested_vehicles(self):
        return self.tested_vehicles
    
    def execute_tests_for_vehicle(self):
        if self.vehicles_to_be_tested:
            vehicle = self.vehicles_to_be_tested.popleft()
            del self.vehicle_lookup[vehicle.tuition]
            for test in vehicle.tests:
                test.result = random.choice([True, False])
            self.tested_vehicles.append(vehicle)
            return vehicle
        return None
    
    def remove_pending_vehicle(self, tuition: str):
        vehicle = self.vehicle_lookup.get(tuition)
        if vehicle:
            self.vehicles_to_be_tested.remove(vehicle)
            del self.vehicle_lookup[tuition]
            return True
        return False

vehicle_manager = VehicleManager()