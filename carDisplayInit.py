class Car(object):
    def __init__(self, price, speed,fuel, mileage,name):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.name = name
        if(self.price> 10000):
            self.tax = .15
        else:
            self.tax = .12
        self.displayInfo()

    def displayInfo(self):
        print "****Inside method display ***"
        print "You are on ", self.name
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

Merzedes = Car(80000,80, 5, 100, "Merzedes")
# Merzedes.displayInfo()