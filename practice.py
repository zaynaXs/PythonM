#import math

#print("Hello World.")
#print("*" * 10)

#string with builts in functions/metthods
#course = "Python Programming"
#print(len(course))
#print(course[0])
#print(course[-1])
#print(course[0:3])
#print(course[0:])
#print(course.upper())
#print(course.find("Pro"))

#Concatenation with formatting
#first = "Zainab"
#last = "Umar"
#full_name = f"{first} {last}"
#full = f"{len(first)} {2 + 2}"
#print(full_name)
#print(full)

#Numbers
X = 1
X = 1.1
X = 1 + 2j #a + bi
#print(10 // 3)
#print(10 ** 3)

#Maths module function/methods
#print(math.ceil(5.2))

#Type convertion
#x = input("x: ")
#y = int(x) + 1
#print(y)
#print(f"x: {x}, y: {y}")

#Built-in Primitive types in Python
#String
#Numbers
#Booleans
#Range is an example of complex primitive types


#Comparison operators with if statement
#print(ord("b"))
#temp = 30
#if temp > 30:
#    print("Stay Hydrated")
#elif temp < 30:
#    print("Stay Warm")
#else:
#    print("It is ok")

#operators/short circuits
#high_income = False
#good_credit = True
#student = True

#if not student:
#    print("eligible")
#else:
#    print("not eligible")

#chaining operator
#age = 22
#if 18 <= age < 65:
#    print("Eligible")


#for loop
#for number in range(1, 4):
    #print("Attempt", number, (number + 1) * ".")

#Exercise
#count = 0
#for x in range(1, 10):
#    if x % 2 == 0:
#        count += 1
#        print(x)
#print(f"We have {count} even numbers")  

#successful = True
#for number in range(3):
#    print("Attempt")
#    if successful:
#        print("Sucessful")
#        break
#else:
#    print("Attempted 3 times and failed")

#Nested loops
#for x in range(5):
    #for y in range(3):
        #print(f"{x}, {y}")

#Iterables range, strings, list

#while loop
#number = 100
#while number > 0:
#    print(number)
#    number //= 2

#command = ""
#while command.lower() != "quit":
#    command = input(">")
#    print("ECHO", command)


#Functions
# 1- perform a task
# 2- return a value

#def greet(name): #parameter is input defined for  func
#    print(f"Welcome aboard {name}")


#greet("Zayn") #arguments is the actual value for the parameter

#def get_greeting(name):
#    return f"Hi {name}"
# by default all function return null by default


#message = get_greeting("ZUS")
#file = open("content.txt", "w")
#file.write(message)

#def increment(number, by=1):
#    return number + by


#print(increment(2))