#  $ Types of Collections:
# List, Tuple, Set, Dictionary
# List it can store multiple values, ordered and changeable into single variable.
list = [1, 3, 4, 5, 6, 7 , 8]
# print(list[0])
# list2 = ["apple", "banana", 8, 9]
# list3 = list()  # just definying empty list
# print(list2[-1]) # to retunr last item in the list

mylist = ["apple", "banana", "kiwi", "melon", "watermelon"]
# print(mylist[1:3]) # ['banana', 'kiwi'] range of items in list

# print(mylist[-3: -1]) # ['kiwi', 'melon']

#  To cahnge items in list:
list2 = ["apple", "cherry", 8, 9]
list2[0] = "grapefruit"
print(list2)

# for i in list2:
#     print(i)

# Check if item exist in the list or not:
# if "banana" in list2:
#     print("Banana is in the list")
# # elif "banana" not in list2: 
# else:
#     print("No banana")

#  Find length of list
# print(len(list2)) # len is function
# list2.append("blackberry") # append in the last
# list2.insert(1,"lemon") # in the middle, just specify which index in the middle which index would be
# print(list2)

#  To remove item from list
# list2.pop(2) 
# print(list2)
#  Also can use del it is keyword not function. If function there is brackets
# mylist3 = [1, 2, 3, 4, 5, 6, 7, 8]
# mylist3.clear()
# print(mylist3)
# del mylist3[0]
# print(mylist3)

# Copy List to Another List. 2 methods
# mylist4 = [1, 2, 3, 4, 5, 6, 7, 8]
# mylist5 = mylist4
# print(mylist4)
# print(mylist5)
# 2 Method to Copy
# mylist6 = mylist5.copy()
# print(mylist6)

#  To join 2 lists
# mylist01 = [1, 2, 3, 4, 5, 6, 7, 8]
# mylist02 = [40, 90, 30]
# mylist03 = mylist01 + mylist02
# print(mylist03)

# for i in mylist02:
#     mylist01.append(i)
# print(mylist01)

# Using extend()
# list01 = [1, 2, 3]
# list02 = ["a", "b", "c"]
# list01.extend(list02)
# print(list01) # [1, 2, 3, 'a', 'b', 'c']














