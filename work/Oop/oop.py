#method- function inside a class

#Question 3
class dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def Bark(self):
        print(self.name,"the",self.breed,"is barking")
d=dog('rocky','labrador')
d.Bark()
        
#Question 4
class laptop:
    def __init__(self,brand,cpu,ram):
        self.brand=brand
        self.cpu=cpu
        self.ram=ram
    def Specs(self):
        print("this laptop is",self.brand,"with",self.cpu,"and",self.ram,"ram")
l=laptop("Dell","Intel i7",16)
l.Specs()

#Question 5
class BankAccount():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,Amount):
        self.Amount=Amount
        self.balance=int(self.balance)+int(self.Amount)
    def show_balance(self):
        print(self.name,"has",self.balance,"rupees")

p=BankAccount('Rahul',1000)
p.deposit(500)
p.show_balance()

#Question 6
class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def accelerate(self):
        self.speed+=20
    def show_speed(self):
        print(self.brand,"is moving at",self.speed,"km/h")
d=Car('Tesla',200)
d.accelerate()
d.show_speed()
    

   
            
        