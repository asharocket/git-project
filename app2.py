# import ecommerce.shipping
# from ecommerce.shipping import calc_shipping
# from ecommerce import shipping
import random


# for i in range(3):
#     print(random.random())

# for i in range(3):
#     print(random.randint(10, 30))

# members = ['Joe', 'Mary', 'Karina', 'Ayaulym', 'Miras']
# leader = random.choice(members)
# print(leader)

# Exercise
# class Dice:
#     def roll(self):
#         num1 = random.randint(1, 6)
#         num2 = random.randint(1, 6)
#         return num1, num2

# dice2 =  Dice()
# print(dice2.roll())

from pathlib import Path
# Absolute Path 
# c:\Program Files\Microsoft Windows
# foir Mac: /usr/local/bin
# relative Path
# path = Path("ecommerce")
# print(path.exists())

# path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())

# path = Path()
# for file in path.glob('*.py'):
#     print(file)

# PyPi Python Index, in that directory you can find hundreds of packages and Pip 

# str = 'India'
# print(str[-1])
# print(str[:-1])
# print(str[::-1])

# kids = ["Ann", "Bob", "Cy"]
# for kid in kids:
#     print("Hi,", kid)

# counts = {}
# for letter in "banana":
#     counts[letter] = counts.get(letter, 0) + 1
#     print(counts)

# from itertools import combinations

# def find_conflicts(bookings):
#     conflicts = []
#     for a, b in combinations(bookings, 2):    # every handshake, once
#         if a["env"] != b["env"]:               # different rooms? skip
#             continue
#         if a["start"] < b["end"] and b["start"] < a["end"]:
#             conflicts.append((a, b))
#     return conflicts

# list1 = ['my', 'name']
# list2 = ['is', 'john']
# print(list1)
# print(list2)

# list3 = list1 + list2
# print(' '.join(list3))


# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# dictionary = zip(list1, list2)
# print(list(dictionary))
# dict1 = dict(zip(list1, list2))
# print(dict1)

# dict2 = {list1[i]: list2[i] for i in range(len(list1))}
# print(dict2)

# dict3 = {}
# for key in list1:
#     for value in list2:
#         dict3[key] = value
#         list2.remove(value)
#         break
# print(dict3)

# class A:
#     count = 0
#     def __init__(self):
#         A.count += 1
#         print('class A is called')

# a1 = A()
# a2 = A()
# a3 = A()
# print(A.count)

# Or
# count = 0
# class B:
#     def __init__(self):
#         global count
#         count += 1
#         print('class B is called')
# b1 = B()
# b2 = B()
# print(count)

