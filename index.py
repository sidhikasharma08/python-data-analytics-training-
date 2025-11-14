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
#exaple1

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

n = int(input("Enter number: "))
i = 1

while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1

#example 2
n = int(input("Enter number: "))
i = 1

while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1

# for loop

#example 1
nums = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]

for num in nums:
    if num &2 == 0:
        print (f"{num} is even")
    else:
        print(f"{num} is odd")

for i in range (1,11):
    print(i)
    #example 2
nums = [3, 6, 2, 8, 4]
total = 0

for n in nums:
    total += n

print("Sum =", total)

    

students_marks = {"Yash": 100 , "Deepak": 12 , "Arun": 9, "Vansh" : 0 , "Anmol" : 1}

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

