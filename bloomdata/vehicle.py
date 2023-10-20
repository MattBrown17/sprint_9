'''
This file holds 2 classes: Vehicle and Convertible.
They are parent and child class.
'''

# imagine these vehicles will be listed on chraig's list
# Parent Class
class Vehicle:
    '''
    This is my class DocString
    '''
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        return "HOOOOOONK"

    def drive(self, miles_driven):
        self.mileage = self.mileage + miles_driven
        return self.mileage

    def __repr__(self):
        return f"A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles"

# Child Class
class Convertible(Vehicle):
    '''
    This is my class docstring
    '''
    def __init__(self, make, model, color, year, mileage, top_down= True):
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return "Top is up"
        self.top_down = True
        return "Top is down"

    def __repr__(self):
        return f"A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles"


if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Camry', 'gray', 2015, 60000)
    print(my_vehicle.mileage)
    print(my_vehicle.honk())
    print(my_vehicle.drive(1204))
    print(my_vehicle)
