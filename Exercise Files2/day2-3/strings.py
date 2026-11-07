# Creating strings diff ways
s = 'welcome'
s = "welcome"
s = str('welcome')
s = str("welcdome")

name = str()
name = ""
name = ''
# print(name)

# Mutable (can change value) 
# Immutable (cannot change the value of variable)
str1 = "welcome"
print(id(str1)) # id of this variable

str1 = str1 + "to python"
print(id(str1))
