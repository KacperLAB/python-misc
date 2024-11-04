#from operations import *

class Car:
    def __init__(self,brand,color,year):
        self.brand = brand
        self.color = color
        self.year = year
    def show(self):
        return (f"{self.brand},{self.color},{self.year}")
class Electric(Car):
    def __init__(self, brand, color, year, battery):
        super().__init__(brand, color, year)
        self.battery = battery
    def show(self):
        return (f"{super().show()},{self.battery}KWh")
class Delivery(Electric):
    def __init__(self, brand, color, year, battery, capacity):
        super().__init__(brand, color, year, battery)
        self.capacity = capacity
    def show(self):
        return (f"{super().show()},{self.capacity}l")
      

#car1 = Car("Audi","Black",2020)
#car2 = Car("BMW","White",2010)
#car3 = Electric("Tesla","Blue",2023,10000)
#car4 = Delivery("VW","Green",2024,50000,400)
#print (car1.show())
#print (car2.show())
#print (car3.show())
#print (car4.show())
    
def print_cars(cars):
    for obj in cars:
        print(obj.show())

def print_electric_cars(cars_e):
    for obj in cars_e:
        print(obj.show())

def create_cars():
    cars = []
    for i in range(1,21):
        cars.append(Car(f"Testowa marka {i}",f"Testowy kolor {i}",i))
    return cars

def create_electric_cars():
    cars_e = []
    for i in range(1,21):
        cars_e.append(Electric(f"Testowa marka {i}",f"Testowy kolor {i}",i,i*10000))
    return cars_e

def main():
    print("Lista zwyklych samochodow")
    print_cars(create_cars())
    print("Lista elektrycznych samochodow")
    print_electric_cars(create_electric_cars())
    
    

if __name__ == '__main__':
    main()