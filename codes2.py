# Exercise 1: List Comprehension Mastery 
# Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.  
words = ["apple", "bat", "cherry", "dog", "elderberry"]
result=[word.upper()for word in words if len(word)>=4]
print(result) 

# Exercise 2: Dictionary Merging with Logic
# Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.
def merge_dictionary(dict_a,dict_b):
    res=dict_a.copy()
    for key,value in dict_b.items():
        if key in res:
            res[key]+=value
        else:
            res[key]=value
    return res  
dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}
merged=merge_dictionary(dict_a,dict_b)
print(merged)

# Exercise 3: Frequency Map with Counter
# Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive. 
from collections import Counter
def count_frequency(text):
    text=text.lower().replace("","")
    return Counter(text)

input_string= "Python Programming"
count=count_frequency(input_string)
print(count)

# Exercise 4: Anagram Checker
# Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).
def is_anagram(word1,word2):
    word1=word1.lower().replace("","")
    word2=word2.lower().replace("","")
    return sorted(word1)==sorted(word2)
word1 = "listen"
word2 = "silent"
print(f'Is {word1} an anagram of {word2} ? {is_anagram(word1,word2)}')

# Exercise 5: Flatten a Nested List
# Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.
def flatten_list(nested):
    result=[]
    for item in nested:
        if isinstance(item,list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
nested = [1, [2, 3], [4, [5, 6]], 7]
print(flatten_list(nested))

# Exercise 6: Reverse Each Word of a String
# Given a sentence, reverse each individual word within the string while maintaining the original word order.
def reverse_string(str1):
    words=str1.split()
    result=[]
    for word in words:
        result.append(word[::-1])
    return " ".join(result)
str1= "Python is awesome"
print(reverse_string(str1))

# Exercise 7: Palindrome Sentence
# Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.

def is_palindrone(sentence):
    cleaned=""
    for char in sentence.lower():
        if char.isalnum():
            cleaned+=char
    return cleaned==cleaned[::-1]
sentence= "A man, a plan, a canal: Panama"
print(f'Is"{sentence}" a palindrome ?{is_palindrone(sentence)}')

# Exercise 8: List Comprehension Filtering (Advanced)
# Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters
# AND they must start with a vowel (a, e, i, o, u).
words=["apple", "education", "ice", "ocean", "python", "umbrella"]
result=[word for word in words if len(word)>5 and word[0].lower()in"aeiou"]
print(result) 

# Exercise 9: Remove Duplicates (Preserving Order)
# Write a function that removes duplicate elements from a list. You cannot use set() because sets do not maintain the original order of elements.

def remove_duplicates(numbers):
    result=[]
    for num in numbers:
        if num not in result:
            result.append(num)
    return result
numbers=[1, 2, 2, 3, 1, 4, 2]
print(remove_duplicates(numbers))

# Exercise 10: Circular Shift (Rotation)	
# Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’.
def shift_list(lst,n,direction):
    if direction=='right':
        return lst[-n:]+lst[:-n]
    else:
        return lst[n:]+lst[:n]
lst=[1,2,3,4,5]
print(shift_list(lst,2,'right'))

# Exercise 11: Dictionary Merging (Value Grouping)
# Merge two dictionaries. If they share a key, the new dictionary should store a list containing values from both dictionaries instead of overwriting the first one.
def merge_dicts(d1,d2):
    result={}
    for key,value in d1.items():
        result[key]=[value]
    for key,value in d2.items():
        if key in result:
            result[key].append(value)
        else:
            result[key]=[value]
    return result
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dicts(d1,d2))

# Exercise 12: Inverted Index
# Create a function that “inverts” a dictionary. Convert a dictionary of Author: [List of Books] into a dictionary of Book: Author
def inverted_index(data):
    result = {}

    for author, books in data.items():
        for book in books:
            result[book] = author

    return result
books_dict = {"Orwell": ["1984", "Animal Farm"],
              "Huxley": ["Brave New World"]}


output = inverted_index(books_dict)
print(output)

# 13	Exercise 13: Dictionary Sorting (Lambda)	Given a list of dictionaries (representing employees), sort them based on their “salary” in descending order using a lambda function.
employees = [
    {"name": "A", "salary": 50},
    {"name": "B", "salary": 70},
    {"name": "C", "salary": 60}
]


result = sorted(employees, key=lambda emp: emp["salary"], reverse=True)

print(result)

# 14	Exercise 14: Subset and Superset Validation	Write a script that takes two lists of integers from a user, converts them to sets, and determines 
# if the first set is a Subset, a Superset, or Disjoint from the second.

# list1 = input("Enter elements of Set A separated by space: ").split()
# list2 = input("Enter elements of Set B separated by space: ").split()
# setA = set()

# for i in list1:
#     setA.add(int(i))

# setB = set()

# for i in list2:
#     setB.add(int(i))

# # Check relationship
# if setA.issubset(setB):
#     print("Set A is a subset of Set B.")

# elif setA.issuperset(setB):
#     print("Set A is a superset of Set B.")

# elif setA.isdisjoint(setB):
#     print("Set A and Set B are disjoint.")

# else:
#     print("Set A and Set B are neither subset, superset, nor disjoint.")

# # 15	Exercise 15: Set Symmetric Difference	Given two lists of student IDs, find the IDs that appear in either the first or the second list, but not in both.     
# list1 = input("Enter Student IDs for List 1: ").split()
# list2 = input("Enter Student IDs for List 2: ").split()

# set1 = set()
# for i in list1:
#     set1.add(int(i))

# set2 = set()
# for i in list2:
#     set2.add(int(i))


# result = set1.symmetric_difference(set2)

# print("Student IDs present in only one list:")
# print(result)

# # Exercise 16: Power Set Generation	
# # Write a function that generates the Power Set of a given set (a set of all possible subsets, including the empty set and the set itself)

# from itertools import combinations

# def power_set(nums):
#     result = []

    
#     for i in range(len(nums) + 1):
#         for subset in combinations(nums, i):
#             result.append(subset)

#     return result

# numbers = [1, 2, 3]

# output = power_set(numbers)

# print(output)

# Exercise 21: Find Duplicates in O(n) Time
#Write a function that identifies all duplicate elements in a list. The solution must run in linear time, meaning you should only traverse the list once.
def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates



numbers = [1, 2, 3, 2, 4, 5, 1, 6]
result = find_duplicates(numbers)
print("Duplicates found:", result)

# Exercise 26: Lambda Sorting with Tuples	
# Given a list of tuples representing employees (Name, Age, Salary), sort the list primarily by Salary in descending order.

employees = [("Alice", 30, 50000),("Bob", 25, 75000),("Charlie", 35, 60000)]
result = sorted(employees, key=lambda emp: emp[2], reverse=True)
print(result)

# Exercise 27: Map and Filter Combination	
# Given a list of numbers, use map() and filter() together to create a list of the squares of only the even numbers.

nums = [1, 2, 3, 4, 5, 6]

result = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))

print(result)

# Exercise 29: Fibonacci Generator (Memory Efficiency)	
# Create a generator function that yields Fibonacci numbers up to N. Instead of returning a full list, it should yield values one by one.
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b

n = 8

print("First", n, "Fibonacci numbers:")

for num in fibonacci(n):
    print(num, end=" ")


# Exercise 30: Custom Context Manager ( with statement)	
# Write a class that acts as a context manager for handling a database-style connection (Don’t do actual database connection, simply printing “Connected” and “Disconnected”). Use the with statement to ensure the connection is closed even if an error occurs.
