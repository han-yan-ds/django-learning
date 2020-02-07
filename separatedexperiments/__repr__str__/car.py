"""
This is a Demo representing how __repr__ and __str__ differ

__repr__ emphasizes unambiguity
__str__ emphasizes readability

print() will always print __str__ if both exist.  It'll print __repr__ if __str__ is missing.
"""

class Car:
    
    def __init__(self, make, model, year, numMiles):
        self.make = make
        self.model = model
        self.year = year
        self.numMiles = numMiles

    def __repr__(self):
        return "%s %s %s with %s miles." % (self.year, self.make, self.model, self.numMiles)

    def __str__(self):
        return "%s %s %s" % (self.year, self.make, self.model)


myFirstCar = Car("Honda", "Prelude", 1996, 84000)

print(myFirstCar)
print(repr(myFirstCar))