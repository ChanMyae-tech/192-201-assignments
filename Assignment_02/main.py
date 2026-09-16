from rental import Vehicle, Renter, ElectricCar, Motorbike
car = Vehicle("Toyota", "Camry", "ABC123")
print(car)
car.rent()
print(car)
car.return_vehicle()
print(car)
renter = Renter("Chan", 528528)
print(renter.name)
print(renter.license_no)
print(renter.rented)

try:
    bad_renter = Renter("", 528528)
except ValueError as e:
    print("Error:", e)

try:
    renter.license_no = -1
except ValueError as e:
    print("Error:", e)

car = Vehicle("Honda", "Civic", "XYZ789")
electric_car = ElectricCar("Tesla", "Model S", "TESLA1", 100)
bike = Motorbike("Yamaha", "R1", "YAM123", 1000)

vehicles = [car, electric_car, bike]
for vehicle in vehicles:
    print(vehicle)
