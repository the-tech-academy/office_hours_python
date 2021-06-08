#Importing abstract methods
from abc import ABC, abstractmethod
#Creating parent class
class car(ABC):
    #Creating regular method
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
    #Creating an abstract method
    @abstractmethod
    def payment(self, amount):
        pass

#Creating child class
class DebitCardPayment(car):
    #Abstracting the parent's method
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $100 limit ".format(amount))

#Creating the object and utilizing it's methods

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
