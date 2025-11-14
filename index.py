# question 01

print("hello world")
a = 4
b = 6
c = a + b

print(c)


age = int(input("enter your age\n"))

if age > 18:
    print ("youre eligible to vote")

else:
    print ("youre not eligible to vote")

# question 02



marks = int(input("enter marks obtained\n"))
if marks >= 95:
    print("A++")
elif marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 35:
    print("D")
else:
    print("fail")


# lists

a = ["Ishu", "Tanishq", "Pulkit", 10]
print(len(a))
print(type(a))

b = ("Ishu", "Tanishq", "Pulkit", 10 , True)
print(len(b))
print(type(b))

c = {"Ishu", "Tanishq", "Pulkit", 10 , 12.60 , False}
print(len(c))
print(type(c))

d = {"Name" : "Ishu Maurya" , "Age" : 17 , "Sex" : "Male" , "Hobby" : "Chilling"}
print(d["Age"])

# loops

# while loop

i = 10
while i > 2:
    i-=1
    print(i)

count = 10
while count > 0:
    if count %2 == 0:
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count -=1

# for loop

nums = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]

for num in nums:
    if num &2 == 0:
        print (f"{num} is even")
    else:
        print(f"{num} is odd")

for i in range (1,11):
    print(i)

students_marks = {"Yash": 100 , "Deepak": 12 , "Arun": -30, "Vansh" : 0 , "Anmol" : 1}

for students, marks in students_marks.items():
    if marks >= 80:
        grade=("a+++++")
    elif marks >= 60:
        grade=("c")
    elif marks >= 10:
        grade=("d")
    else:
        grade=("failed")
    print(f"{students} scored {marks} and grade {grade}.") 

# functions

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


class dog (Animal):
    def speak(self):
        print("Cow moos")

dog = dog()
dog.speak()  

class animal:
    def speak(self):
        print("animals make different sounds")

class dog(animal):
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
