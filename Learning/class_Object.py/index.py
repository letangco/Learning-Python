class Person:
    x = 5

p1 = Person()

print(p1.x)

print('-----------------------------------')
class Car:
    def __init__(self, year, model, money):
        super().__init__()
        self.year = year
        self.model = model
        self.money = money
    def exportFunctionCar(self):
        print('This is super Car, model is '+ self.model+ ' - ' + self.year+ ' with ' + self.money)


my_car = Car('2015', 'Mercerdes', '250.000$')
my_car.exportFunctionCar()
