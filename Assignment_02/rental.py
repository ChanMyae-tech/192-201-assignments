class Vehicle:
    def __init__(self, make, model, plate):
        self.make = make
        self.model = model
        self.plate = plate
        self.is_rented = False

    def rent(self):
        self.is_rented = True
    def return_vehicle(self):
        self.is_rented = False
    def __str__(self):
        if self.is_rented:
            status = "Rented"
        else:
            status = "Available"
        return f"{self.make} {self.model} ({self.plate}) - {status}"


class Renter:
    def __init__(self,name, license_number):
        self.name = name
        self.license_number = license_number
        self.rented = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be empty")
        self._name = value
    @property
    def license_number(self):
        return self._license_number
    @license_number.setter
    def license_number(self, value):
        if value <= 0:
            raise ValueError("License number must be positive")
        self._license_number = value
class ElectricCar(Vehicle):
    def __init__(self, make, model, plate, battery_kwh):
        super().__init__(make, model, plate)
        self.battery_kwh = battery_kwh

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - Battery Capacity: {self.battery_kwh} kWh"

class MotorBike(Vehicle):
    def __init__(self, make, model, plate, engine_cc):
        super().__init__(make, model, plate)
        self.engine_cc = engine_cc

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - Engine Size: {self.engine_cc} cc"
