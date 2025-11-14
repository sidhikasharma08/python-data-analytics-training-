# functions

#example1
def fn():
    print("hello world")
fn()


def me(name):
    print(f"my name is {name}")
me("sidhika")

def operation(n,m):
    return n*n, n-m, n/m

s = operation(11,10) 
print(s)

def store():

    import person

a=person.person1["alice"]
print(a)

#example2
def check_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(7))


# modules

import person

print(person.greet())


import random

print("random number between 1-10:", random.randint(1,10))
colors = ["wine", "sea green", "turmeric yellow", "turkish blue", "baby pink"]

print("random color:", random.choice(colors))

import datetime

today = datetime.date.today()
print("yesterday's date:", today)

now = datetime.datetime.now()
print("current time:", now)

import sys
print("python version:", sys.version)
print("platform:", sys.platform)

import math

print("power of 3^4:", pow(3,4))
print("square root of 49:", math.sqrt(49))
print("value of pi:", math.pi)
print("ceil of 4.3:", math.ceil(4.3))
print("floor of 4.8:", math.floor(4.8)) 

#task

def r():
    import random
    a = random.randint(-100,100)
    print(f"random numbe btw -100 to 100:{a}")

    if a <0:
        print("it is negative")
    else:
        print("it is positive")

    if a%5 == 0:
        print("it is divisible by 5")
    elif a%5 != 0:
        print("not divisible by 5")

    if a%2 == 0:
        print("it is even")
    else:
        print("it is odd") 

r()


class person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
p1= person("sidhika", 17)
print(p1.name, p1.age)

class person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"my name is {self.name} and i am {self.age} years old.")
result = person("anurag", 19)
result.greet()


class Rectangle:
    def __init__(self, length, breadth):

        self.length = length
        self.breadth = breadth

    def area(self):

        return self.length * self.breadth

try:
    user_length = float(input("Enter the length of the rectangle: "))
    user_breadth = float(input("Enter the breadth of the rectangle: "))

    my_rectangle = Rectangle(user_length, user_breadth)

    calculated_area = my_rectangle.area()
    print(f"The area of the rectangle is: {calculated_area}")

except ValueError:
    print("Invalid input. Please enter numerical values for length and breadth.")

class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving.......!!!!!!")


car1= car("bmw", "black")
car2= car("tesla", "white")

car1.drive()
car2.drive() 

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("sidhika", 17)
print(p1.name)
print(p1.age)


class Animal:
    def speak(self):
        print("Animal speaks")


class cow (Animal):
    def speak(self):
        print("Cow moos")

cow = cow()
cow.speak()  

class animal:
    def speak(self):
        print("animals make different sounds")

class cow(animal):
    def speak(self):
        print("cow moos")

class cat(animal):
    def speak(self): 
        print("cat meows")

for pet in ((dog),cat()):
    pet.speak()

import pandas as pd

data = [10,20,30,40]
s=pd.Series(data)

print(s)


data = {
    "name" : ["sidhika", "tannu" , " ishu", "pulkit"],
    "age" : [17, 18, 17, 22],
    "marks" : [48, 78, 89 , 76]
}

df = pd.DataFrame(data)
print(df)

calories = {"day1": 400, "day2": 380, "day3": 390}
dt = pd.Series(calories)

print(dt) 

