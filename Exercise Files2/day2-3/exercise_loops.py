# You have test case IDs from 1 to 5.

# Using a for loop:

# Print each as TC_001, TC_002, … TC_005
# Hint: f"TC_{i:03d}"

# for i in range(1, 6):
#     print(f"TC_{i:03d}")

######################
"""Print numbers from 1 to 5 using a for loop.
Expected output:
1
2
3
4
5
Hint: for i in range(1, 6):"""
# for i in range(1,6):
#     print(i)

################### 
"""Print each browser name from this list:


browsers = ["chrome", "firefox", "edge"]
Expected:


chrome
firefox
edge
"""
browsers = ["chrome", "firefox", "edge"]

# for i in browsers:
#     print(i)

"""Print "Running test" 3 times using range.

Expected:


Running test
Running test
Running test
"""
# for i in range(3):
#     print("Running test")

"""Print numbers 1 to 3 using a while loop.
Start with:
i = 1
Expected:

1
2
3
"""

# i = 1
# while i <= 3:
#     print(i)
#     i = i + 1

'''Exercise 5 — while loop (easy)
Print "Retry" 2 times using a while loop.
Start with:
count = 1
Expected:
Retry
Retry
'''
# count = 1
# while count <= 2:
#     print("Retry")
#     count = count + 1

'''Exercise 6 — for loop (easy)
Given:
statuses = [200, 404, 500]
Print each status like:
Status: 200
Status: 404
Status: 500
'''
statuses = [200, 404, 500]
# for i in statuses:
#     print(f"Status {i}")

'''Given:
results = ["pass", "fail", "pass"]
Print "Found a bug" only when the result is "fail".
Expected:
Found a bug
'''

# results = ["pass", "pass", "pass"]
# for result in results:
#     if result == "fail":
#         print("Found a bug")
#     else:
#         print("no bugs")

'''Start with:
attempt = 1
Using while attempt <= 3:
if attempt == 3, print "PASS"
else print "Trying..."
then increase attempt
Expected:
Trying...
Trying...
PASS
'''
# attempt = 1
# while attempt <= 3:
#     if attempt == 3:
#         print("PASS")
#     else:
#         print("Trying...")
#     attempt = attempt + 1

'''
tests = ["login", "search", "logout"]
Expected:
1. login
2. search
3. logout
Hint: use enumerate(tests, start=1) or a counter.
Write it, or say “answer”.
'''
# tests = ["login", "search", "logout"]
# i = 1
# for name in tests:
#     print(f"{i}. {name}")
#     i = i + 1
# tests = ["login", "search", "logout"]
# for i, name in enumerate(tests, start=1):
#     print(f"{i}. {name}")

'''Keep asking for a password until the user types "qa123".
Hint:
password = ""
while password != "qa123":
    password = input("Enter password: ")
print("Access granted")
'''
# password = ""
# while password != "qa123":
#     password = input("Enter password: ")
# print("Access granted")

# Print even numbers:
for i in range(2,7,2):
    print(i)