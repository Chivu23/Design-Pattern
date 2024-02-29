"""

Example:
STRUCTURAL Design Patterns:
___PROXY DP___

"""

# it helps us control and manage access to the objects we protect

from abc import ABC, abstractmethod


class AbstractCar(ABC):

    @abstractmethod
    def drive(self):
        pass

class Car(AbstractCar):
    def drive(self):
        print("You are driving the car.")


class Driver:
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstractCar):
    def __init__(self, driver: Driver):
        self.car = Car()
        self.driver = driver

    def drive(self):
        if self.driver.age < 18:
            print("Sorry little driver, you are too young to drive.")
        else:
            self.car.drive()


driver = Driver(16)
print(driver.age)
# If directly instantiate the Car class => no constraint on age

car = Car()
car.drive()

# If instantiate ProxyCar, the age of the driver is checked

proxy_car = ProxyCar(driver)
proxy_car.drive()

new_driver = Driver(20)
proxy_car = ProxyCar(new_driver)
proxy_car.drive()


