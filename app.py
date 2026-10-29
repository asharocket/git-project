# name = input('What is your name? ')
# fav_color = input("What's your favourite color? ")
# print(name + ' likes ' + fav_color)
# int(), float(), bool()

# birth_year = input('Brith year: ')
# print(type(birth_year))
# age = 2026 - int(birth_year)
# print(type(age))
# print(age)

# weight = input('Weight(lbs): ')
# inKg = 0.45 * float(weight)
# print('In kg: ' + str(inKg))

# course = ''' 
# Hi John,

# Here is our first email.
# Thank you.

# Best,
# Team
# '''

# course = 'Python for Beginners'
# print(course[0:3])

#Concatneated & Formatted Strings:
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder' 
# msg = f'{first} [{last}] is a coder'
# # print(message)
# print(msg)

# String Methods
# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.replace('Beginners', 'Absolute Beginners'))
# print(course.replace('P', 'J'))
# print('Python' in course)

# Arthimetic Methods
# print(10 ** 3)
# print(10 ** 3)
#Augmented assignment operator, shorter
# x = 10
# x -= 3
# print(x)
#Operator Precedence: exponentiation **, multiliplication or division, addition or substraction

# If Statements
# weather = input("What's the weather like today? ")
# is_hot = False
# if is_hot == True:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_hot == False:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")

# Exercise for if Statements
# price = 1000000
# buyer_credit = True

# if buyer_credit == True:
#     down_payment = price * 0.1
# else:
#     down_payment = price * 0.2
# print(f"Down payment: ${down_payment}")

# Logical Operators( If applicant has high income AND good credit, then eligible for loan)
# and, or, and not - operators
# has_high_income = True
# has_good_credit = False

# if has_high_income or has_good_credit:
#     print('Buyer is eligible for loan')
# else:
#     print('Not eligible for loan')

# Comparison operators, != not equal
# temparature = 20
# if temparature >= 30:
#     print("it's a hot day")
# elif temparature < 10:
#     print("It's a cold day")
# else:
#     print("it's neither hot not cold")

# name = input("Name: ")
# if len(name) < 3:
#     print('Name must be 3 characters long')
# elif len(name) > 20:
#     print('Name must be less than 30 charaters long')
# else:
#     print('name looks good')

# Weight Conferter
# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')

# if unit.upper == 'L':
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else: 
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

# While Loops - to execute a block of code multiple times
# i = 1
# while i <= 6:
#     print('*' * i)
#     i = i + 1
# print("Done")

# Guessing game:
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("Guessed it right")
#         break
# else:
#     print("Sorry, you guessed wrong")

#car game:
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Already started")
#         else:
#             started = True
#             print("Car has started...")
#     elif command == "stop":
#         if not started:
#             print("Car has already stopped")
#         else:
#             started = False
#             print("Car stopped")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit        
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't undertsand that")

# For loops (iterate over collection)
# for item in 'Python':
#     print(item)
# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)
# below 3rd number is steps forward between them
# for item in range(5, 10, 2):
#     print(item)

# exercise:
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     #total = total + price. OR the same thing but augmented below
#     total += price
# print(f"Total: {total}")
 
# Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f" ( {x}, {y})")
# Exercise to generate X-s
# numbers = [5, 2, 5, 2, 2]
# x = 0
# for x_count in numbers:
#     # print('x' * x_count)
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

#Index of 1st item, -1 last item from end. the list is not modified
# names = ['John', 'Mosh', 'Sarah', 'Bob']
# print(names[-1])
# print(names[1:-2])
# To modify
# names[0] = 'Johne'
# print(names)

# Write a program to find the largest number in a list
numbers = [2, 5, 17, 90, 909]
# print(numbers)
# print(max(numbers))
# max_number = numbers[0]
# for number in numbers:
#     # print(numbers[:])
#     if number > max_number:
#         max_number = number
# print(max_number)
# 2D Lists / Two-dimential lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][0] = 20
# print(matrix[0][0])
# for row in matrix:
#     for item in row:
#         print(item)
# List Methods
# numbers = [5, 3, 3, 6, 7]
# numbers.append(20)
# print(numbers)
# numbers.insert(0, 34)
# print(numbers)
# numbers.remove(6)
# print(numbers)
# numbers.clear()
# print(numbers)
# print(50 in numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# print(numbers2)

# Exercise: Write a program to remove the duplicates in a list
# list = [4, 5, 6, 4, 7, 6, 8, 9]
# uniques = []
# for i in list:
#     if i not in uniques:
#             uniques.append(i)
# print(uniques)

# Tuples, similar to Lists, but unlike Lists we cannot modify them. Immutable
# numbers = (1, 2, 3)
# print(numbers[0])

# A powerful feature called Unpacking
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# or use this below using tuple
# x, y, z = coordinates
# print(y)
##########################
# Dictionaries to store information as key-value pairs, keys should be unique
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": "True"
# }
# print(customer["name"])
# print(customer.get("Birthdate", "Jan 3, 1980"))
# customer["birthdate"] = "Jan 3, 1981"
# print(customer)

# Exercise:
# phone = input("Phone: ")
# numbers = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# outputs = ""     
# # print(numbers[1])
# for ch in phone:
#     outputs += numbers.get(ch, "!") + " "
# print(outputs)

# Functions. A functions is a container for a few lines of code that perform specific task
# def greet_user():
#     print('Hi there! Welcome')


# print('Start')
# greet_user()

# Parameters - Passing information to a Function. 
# Parameters are Placeholders in our function for receiving information, Here 
# and Arguments are actual pieces of information that we supply to these functions

# def greeting_user_name(first_name, last_name):
#     print(f"Hi, {first_name} {last_name}")


# greeting_user_name("Karoline", "Steffon")

# Keyword Arguments.

# greeting_user_name("Brown", "Layla")
# greeting_user_name(last_name="Koko", first_name="Georgina")

# Return Statement

# def square(number):
#     return number * number


# result = square(3)
# print(square(3))

# Exercise

# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😄",
#         ":(": "🥺"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# print(emoji_converter("From :( and To :)"))

# Exceptions. exit code 0 means success, exit code 1 means crash
# try:
#     age = int(input('Age: '))
#     print(age)
#     income= 20000
#     risk = income / age
# except ValueError:
#     print('Invalid value')
# except ZeroDivisionError:
#     print('Value cannot be 0')

# Classes - important, and not specific to Python and 
# lots of other prog lang-s do support notion of classes 
# We use classes to define new types
# Numbers, Strings, Booleans, Lists, Dictionaries
# for classes we use Pascal naming conventions, by capitial first letter of words: EditName
#In Class there could different methods functions belonging to it. Definition of Point class
# Object is an instance of a class, a class simply defines the blueprint for creating objects
# And Objects/Instances are actual instances of that blueprint
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         pass
#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
# A part of methods Class can have attributes/ variables that belong to a particular object. 

# point2 = Point()
# print(point2.x)

# Constructors
# point = Point(10,20)
# point.x = 11
# print(point.x)

# Exercise
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, I'm {self.name}")

# john = Person("Jay")
# john.talk()

# bob = Person("Bob Smith") 
# bob.talk()
#In programming there is concept DRY - Don't Repeat Yourself
# Inheritance
# class Mamaal:
#     def walk(self):
#         print("walk")

# class Dog(Mamaal):
#     def bark(self):
#         print("bark")

    
# class Cat(Mamaal):
#     # pass
#     def be_annoying(self):
#         print("annoying")


# dog1 = Dog()
# dog1.bark()
# cat1 = Cat()
# cat1.be_annoying()

# Modules. A file with Python code, we use modules to keep our code in files

# import converters
# print(converters.lbs_to_kg(143))

# from converters import lbs_to_kg
# print(lbs_to_kg(146))

from utils import find_max
numbers = [1, 4, 698, 70, 200]
print(find_max(numbers))
