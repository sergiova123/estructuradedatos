from fastapi import FastAPI
from models import Vehicle
from classes import vehicle_manager as vm

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is up and running"}

@app.post("/register")
def register(vehicle: Vehicle):
    vm.add_vehicle(vehicle)
    return {"data": vehicle.dict(), "message": "Vehicle registered successfully"}

@app.get("/vehicles/pending")
def get_pending_vehicles():
    vehicles = vm.get_vehicles_to_be_tested()
    return {"pending_vehicles": [vehicle.dict() for vehicle in vehicles]}

@app.get("/vehicles/tested")
def get_tested_vehicles():
    vehicles = vm.get_tested_vehicles()
    return {"tested_vehicles": [vehicle.dict() for vehicle in vehicles]}

@app.post("/vehicles/execute-tests")
def execute_tests():
    vehicle = vm.execute_tests_for_vehicle()
    if vehicle:
        return {"vehicle": vehicle.dict(), "message": "Tests executed successfully"}
    return {"message": "No pending vehicles to test"}

@app.delete("/vehicles/{tuition}/remove")
def remove_vehicle(tuition: str):
    vehicle_removed = vm.remove_pending_vehicle(tuition)
    if vehicle_removed:
        return {"message": "Vehicle removed successfully"}
    return {"message": "Vehicle not found or not pending"}