# list = ['india', 'is', 'my', 'country']

# str = ''.join(list)
# print(str)
# duplicates = []

# for char in str:
#     if str.count(char)>1 and char not in duplicates:
#         duplicates.append(char)

# print(duplicates)

############################
# str = 'test'
# unique = []
# for char in str:
#     if str.count(char) == 1 and char not in unique:
#         unique.append(char)

# print(unique)
##########################
# list = ['india', 'is', 'my', 'country']
# l2 = []
# for word in list:
#     if word.startswith('i'):
#         l2.append(word)
# print(l2)
############################
# Find the biggest number
# numbers = [983, 5, 70, 909]
# max = 0
# for i in numbers:
#     if i > max:
#         max = i

# print(max)
#########################
# s ="hey"
# def reverse_string_loop(s):
#     result = ""
#     for ch in s:
#         result = ch + result     # new bead goes in FRONT
#     return result

# print(reverse_string_loop(s))

########################
# from collections import Counter
# print(Counter("banana"))
# s = 'apple'
# def char_count(s):
#     counts = {}
#     for ch in s:
#         counts[ch] = counts.get(ch, 0) + 1
#     return counts

# print(char_count(s))

# from collections import Counter

# def first_unique(s):
#     counts = Counter(s)
#     for ch in s:
#         if counts[ch] == 1:
#             return ch
#     return None        # everybody has a twin

# print(first_unique("swiss"))   # w

# print(sorted("ley"))
# s = 'ball'
# print(s[::-1])

# s = 'A man, a plan, a canal: Panama'
# def is_palindrome(s):
#     cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
#     return cleaned == cleaned[::-1]

# print(is_palindrome(s))

# s = "Quality Assurance"
# unique = []
# for ch in s:
#     if ch not in unique and s.count(ch) == "aeiou":
#         unique.append(ch)
# print(unique)


# def count_vowels(s):
#     count = 0
#     for ch in s.lower():
#         if ch in 'aeiou':
#             count += 1
#     return count

# print(count_vowels(s))
# with open("test.txt", "w") as f:
#     f.write("Hello World")

# with open("test.txt", "r") as f:
#     content = f.read()
#     print(content)
# @pytest.fixture
# def sample_data():
#     print("\n Steup: Creating test data")
#     data = {"name": "Ray", "age": 43}
#     return data

# def tes_1(sample_data):
#     assert sample_data["name" ]== "Ray"
#     assert sample_data["age" ]== 43
#     print("Pass")