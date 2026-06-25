print('Hello Python')


#Sum of two numbers
a=int(input('enter the first number: '))
b=int(input('enter the second number: '))
c=a+b
print('the sum of the two numbers is: ',c)

#To check the number is even or odd
num=int(input('enter the number: '))
if num%2==0:
    print('The number is Even')
else:
    print('The number is Odd')

#Positive, Negative, or Zero
'''Write a program to determine whether a number is:Positive
Negative,Zero'''
numb=int(input('enter the number: '))
if numb>0:
    print('The number is Positive')
elif numb<0:
    print('The number is Negative')
else:
    print('The number is zero')

#largest of two numbers
n1=int(input('enter the first number: '))
n2=int(input('enter the second number: '))
if n1>n2:
    print('The Largest number is:',n1)
else:
    print('The Largest number is:',n2 )

#Print the multiplication table of given number
num1=int(input('enter the number: '))
for i in range(1,11):
    print(num1,'x',i,'=',num1*i)

#Sum of numbers from 1 to n
n=int(input('enter the number: '))
sum=0
for i in range(1,n+1):
    sum=sum+i
print('The sum of numbers from 1 to',n,'is:',sum)

#Count the Even number

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_count=0
for n in numbers:
    if n%2==0:
        even_count+=1
print('The count of Even numbers is:',even_count)

#Take a string as input and reverse it
str=input('enter The String: ')
reversed_str=str[::-1]
print('The Reversed String Is:',reversed_str)

#Find Largest Number in a List

number = [12, 45, 3, 67, 22]
number.sort()
Largest=number[-1]
print('The Largest Number in the list is:',Largest)

#Create a Function for Addition
#Write a function named add() that accepts two numbers and returns their sum.
def add(num1,num2):
    num3=num1+num2
    return num3
num1=int(input('enter the first number: '))
num2=int(input('enter the second number: '))
result=add(num1,num2)
print('The sum of the two numbers is:',result)

#Write a function that accepts a number and returns:
# True if even
# False if odd
def is_even(number):
    if number%2==0:
        return True
    else:
        return False
number=int(input('enter the number: '))
if is_even(number):
    print('The number is Even')
else:
    print('The number is Odd')

#Count Elements in a List
def  count_elements(lst):
    return len(lst)

fruits = ["apple", "banana", "orange", "apple", "grapes"]
count = count_elements(fruits)
print("The count of elements in the list is:", count)

#Create a dictionary:
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}
print(student)

#student Class
# Create a class named Student with:name attribute age attribute
# Create an object and display both values.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
student1=Student('Aryan',22)
student1.display()

#Find Factorial of a Number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input('enter the number: '))
result=factorial(num)
print('The factorial of the number is:',result)

#Count Vowels in a String
def count_vowels(string):
    count=0
    for char in string:
        if char.lower() in 'aeiou':
            count+=1
    return count

str=input('enter the string: ')
vowel_count=count_vowels(str)
print('The count of vowels in the string is:',vowel_count)

#Remove Duplicates from a List

l=[1, 2, 2, 3, 4, 4, 5]
unique_list=list(set(l))
print('The list after removing duplicates is:',unique_list)

#Read and Write a File
# Create a text file, write "Python Training" into it, and read the content back.
file=open('sample.txt','w')
file.write('Python Training')
file.close()
file=open('sample.txt','r')
text=file.read()
print('The content of the file is:',text)

#Handle Division by Zero
def handle_zero_division(n1,n2):
    try:
        result=n1/n2
        return result
    except ZeroDivisionError:
        return 'Error: Division by zero is not allowed.'
n1=int(input('enter the first number: '))
n2=int(input('enter the second number: '))
result=handle_zero_division(n1,n2)
print('The result of division is:',result)

#List Exercises	Exercise 1: Perform Basic List Operations
l1=[1,2,3,4,5]
print('Original List:',l1)
l1.append(6)
print('List after appending 6:',l1)
l1.remove(3)
print('List after removing 3:',l1)
l1.insert(2,10)
print('List after inserting 10 at index 2:',l1)

#Exercise 2: Perform List Manipulation
l2=[10,20,30,40,50]
print('Original List:',l2)
l2.reverse()
print('List after reversing:',l2)

#Exercise 3: Sum and average of all numbers in a list
l3=[5,10,15,20,25]
sum = 0
for i in l3:
    sum +=i
average_of_list=sum/len(l3)
print('The sum of the list is:',sum)
print('The average of the list is:',average_of_list)

#Exercise 4: Reverse a list
l4=[1,2,3,4,5]
l4.reverse()
print('The reversed list is:',l4)

#Turn every item of a list into its square
li=[2,3,4,5,6]
squared_list=[x**2 for x in li]
print('The squared list is:',squared_list)

#Exercise 6: Find Maximum and Minimum
l5=[10,20,5,15,25]
l5.sort()
maximum=l5[-1]
minimum=l5[0]
print('The maximum number in the list is:',maximum)
print('The minimum number in the list is:',minimum)

#Exercise 7: Count Occurrences of an Element
l6=[1,2,3,4,2,5,2]
element=int(input('enter the element to count: '))
count=l6.count(element)
print('The count of the element in the list is:',count)


#Exercise 8: Sort a List
l8=[5,2,9,1,5,6]
l8.sort()
print('The sorted list is:',l8)

#Exercise 9: Create a copy of a list
l9=[1,2,3,4,5]
copy_of_l9=l9.copy()
print('The copy of the list is:',copy_of_l9)    

#Exercise 10: Combine two lists
li=[1,2,3]
li2=[4,5,6]
combined_list=li+li2
print('The combined list is:',combined_list)

#Exercise 11: Remove empty strings from the list of strings
l1=['Hello', '', 'World', '', 'Python'] 
for s in l1:
    if s=='':
        l1.remove(s)
print('The list after removing empty strings is:',l1)

#Exercise 12: Remove Duplicates from list
l7=[1,2,2,3,4,4,5]
unique_list=list(set(l7))
print('The list after removing duplicates is:',unique_list)

#Exercise 13: Remove all occurrences of a specific item from a list
l10=[1,2,3,4,2,5,2]
item=int(input('enter the item to remove: '))
while item in l10:
    l10.remove(item)
print('The list after removing all occurrences of the item is:',l10)

#Exercise 14: List Comprehension for Numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print('The squared numbers are:',squared_numbers)

#Exercise 15: Access Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
for sublist in nested_list:
    for item in sublist:
        print(item)

#Exercise 16: Flatten Nested List
nested_list = [[1, 2], [3, 4], [5, 6]]
for sublist in nested_list:
    for item in sublist:
        print(item, end=' ')

#Exercise 17: Concatenate two lists index-wise
list1 = ['A', 'B', 'C']
list2 = ['1', '2', '3']  
res = [] 
for i in range(len(list1)):
    res.append(list1 + list2)
print(res)   

#Exercise 19: Iterate both lists simultaneously
list1 = ['A', 'B', 'C']
list2 = [1, 2, 3]
for i in range(len(list1)):
    print(list1[i], list2[i])

#Exercise 21: Add new item to list after a specified item
l11=[1,2,3,4,5]
item=int(input('enter the item to add: '))  
after_item=int(input('enter the item after which to add: '))
if after_item in l11:
    index=l11.index(after_item)
    l11.insert(index+1,item)
    print('The list after adding the new item is:',l11)

#Extend nested list by adding the sublist
nested_list = [[1, 2], [3, 4], [5, 6]]
new_sublist = [7, 8]
nested_list.append(new_sublist)
print('The nested list after adding the new sublist is:',nested_list)

#: Replace list’s item with new value if found
l12=[1,2,3,4,5]
old_value=int(input('enter the old value to replace: '))
new_value=int(input('enter the new value: '))
if old_value in l12:
    index=l12.index(old_value)
    l12[index]=new_value
    print('The list after replacing the item is:',l12)

#Python Dictionary	Exercise 1: Perform basic dictionary operations
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}
print('Original Dictionary:',student)
student["age"]=21
print('Dictionary after updating age:',student)
student["grade"]="A"
print('Dictionary after adding grade:',student)
del student["course"]
print('Dictionary after deleting course:',student)

#Exercise 2: Perform dictionary operations
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}
print('Original Dictionary:',student)
print('Keys:',student.keys())
print('Values:',student.values())

#Exercise 3: Dictionary from Lists
keys = ['name', 'age', 'course']
values = ['Alice', 22, 'Data Science']
for i in range(len(keys)):
    student[keys[i]] = values[i]
print('Dictionary from lists:',student)

#Exercise 4: Clear Dictionary
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}
student.clear()
print('Dictionary after clearing:',student)

#Exercise 5: Merge two Python dictionaries into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print('Merged Dictionary:',dict1)

#Exercise 6: Count Character Frequencies
text = "hello world"
char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1
print('Character Frequencies:',char_freq)

#Exercise 7: Access Nested Dictionary
nested_dict = {"student": {"name": "John", "age": 20}}
print('Accessing Nested Dictionary:',nested_dict["student"]["name"],nested_dict["student"]["age"])

#Exercise 8: Print the value of key ‘history’ from nested dict
nested_dict={"student": {"name": "John", "age": 20, "history": "A"}}
print('The value of key history is:',nested_dict["student"]["history"])

#Exercise 9: Modify Nested Dictionary
nested_dict={"student": {"name": "John", "age": 20, "history": "A"}}
nested_dict["student"]["history"] = "B"
print('Modified Nested Dictionary:',nested_dict)

#Exercise 10: Initialize dictionary with default values
keys = ['name', 'age', 'course']
for key in keys:
    student[key] = None
print('Dictionary with default values:',student)

#Exercise 11: Create a dictionary by extracting the keys from a given dictionary
d = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]

result = {}

for key in keys:
    result[key] = d[key]

print(result)

#Exercise 12: Delete a list of keys from a dictionary
d = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_to_delete = ["b", "d"]
for key in keys_to_delete:
    del d[key]
print('Dictionary after deleting keys:',d)

#Exercise 13: Check if a value exists in a dictionary
d = {"a": 1, "b": 2, "c": 3, "d": 4}
value_to_check = 3
if value_to_check in d.values():
    print('The value exists in the dictionary.')
else:
    print('The value does not exist in the dictionary.')

#Exercise 14: Rename key of a dictionary
d = {"a": 1, "b": 2, "c": 3}
old_key = "b"
new_key = "x"
if old_key in d:
    d[new_key] = d.pop(old_key)
print('Dictionary after renaming key:',d)

#Exercise 15: Get the key of a minimum value
d = {"a": 1, "b": 2, "c": 3, "d": 0}
min_key = min(d, key=d.get)
print('The key of the minimum value is:',min_key)

#Exercise 16: Change value of a key in a nested dictionary
nested_dict = {"student": {"name": "John", "age": 20}}
nested_dict["student"]["age"] = 21
print('Nested Dictionary after changing value:',nested_dict)

#Exercise 17: Invert Dictionary
d = {"a": 1, "b": 2, "c": 3}
inverted_dict = {v: k for k, v in d.items()}
print('Inverted Dictionary:',inverted_dict)

#Exercise 18: Sort Dictionary by Keys
d = {"b": 2, "a": 1, "c": 3}
sorted_dict = dict(sorted(d.items()))
print('Dictionary sorted by keys:',sorted_dict)

#Exercise 19: Sort Dictionary by Values
d = {"b": 2, "a": 1, "c": 3}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print('Dictionary sorted by values:',sorted_dict)

#Exercise 20: Check if All Values are Unique
d = {"a": 1, "b": 2, "c": 3, "d": 2}
if len(d.values()) == len(set(d.values())):
    print('All values are unique.')
else:
    print('Not all values are unique.')

#Python Tuples	Exercise 1: Perform Basic Tuple Operations
t1 = (1, 2, 3, 4, 5)
print('Original Tuple:', t1)
print('Length of the tuple:', len(t1))
print('Maximum value in the tuple:', max(t1))

#Exercise 2: Tuple Repetition
t2 = (1, 2, 3)
repeated_tuple = t2 * 3
print('Repeated Tuple:', repeated_tuple)

#Exercise 3: Slicing Tuples
t3 = (1, 2, 3, 4, 5)
sliced_tuple = t3[1:4]
print('Sliced Tuple:', sliced_tuple)

#Exercise 4: Reverse the tuple
t4 = (1, 2, 3, 4, 5)
reversed_tuple = t4[::-1]
print('Reversed Tuple:', reversed_tuple)

#Exercise 5: Access Nested Tuples
nested_tuple = (1, 2, (3, 4), 5)
print('Accessing Nested Tuple:', nested_tuple[2][0], nested_tuple[2][1])    

#Exercise 6: Create a tuple with single item 50
single_item_tuple = (50,)
print('Single Item Tuple:', single_item_tuple)

#Exercise 7: Unpack the tuple into 4 variables
t5 = (1, 2, 3, 4)
a, b, c, d = t5
print('Unpacked Values:', a, b, c, d)

#Exercise 8: Swap two tuples
t6 = (1, 2, 3)
t7 = (4, 5, 6)
t6, t7 = t7, t6
print('Swapped Tuples:', t6, t7)

#Exercise 9: Copy Specific Elements From Tuple
t8 = (1, 2, 3, 4, 5)
new_tuple = t8[1:4]
print('New Tuple with specific elements:', new_tuple)

#Exercise 10: List to Tuple
l = [1, 2, 3, 4, 5]
t9 = tuple(l)
print('List converted to Tuple:', t9)

#Exercise 11: Function Returning Tuple
def get_coordinates():
    x = 10
    y = 20
    return (x, y)

coordinates = get_coordinates()
print('Coordinates:', coordinates)

#Exercise 12: Comparing Tuples
t10 = (1, 2, 3)
t11 = (1, 2, 4)
if t10 < t11:
    print('t10 is less than t11')
elif t10 > t11:
    print('t10 is greater than t11')
else:
    print('t10 is equal to t11')

#Exercise 13: Removing Duplicates from Tuple
t12 = (1, 2, 2, 3, 4, 4, 5)
unique_tuple = tuple(set(t12))
print('Tuple after removing duplicates:', unique_tuple)

#Exercise 14: Filter Tuples
t13 = (1, 2, 3, 4, 5)
even_tuple=()
for num in t13:
    if num % 2 == 0:
        even_tuple += (num,)
print('Filtered Tuple with even numbers:', even_tuple)

#Exercise 15: Map Tuples
t14 = (1, 2, 3, 4, 5)
squared_tuple = tuple(map(lambda x: x**2, t14))
print('Squared Tuple:', squared_tuple)

#Exercise 16: Modify Tuple
t15 = (1, 2, 3, 4, 5)
# Convert to list, modify, and convert back to tuple
l = list(t15)
l[2] = 10
modified_tuple = tuple(l)
print('Modified Tuple:', modified_tuple)

#Exercise 17: Sort a tuple of tuples by 2nd item
t16 = ((1, 'b'), (2, 'a'), (3, 'c'))
sorted_tuple = tuple(sorted(t16, key=lambda x: x[1]))
print('Tuple sorted by 2nd item:', sorted_tuple)

#Exercise 18: Count Elements
t17 = (1, 2, 3, 2, 4, 5, 2)
element_to_count = 2
count = t17.count(element_to_count)
print('Count of the element in the tuple:', count)

#Exercise 19: Check if all items in the tuple are the same
t18 = (1, 1, 1, 1)
if all(x == t18[0] for x in t18):
    print('All items in the tuple are the same.')
else:
    print('Not all items in the tuple are the same.')   

#Python Sets Exercise 1: Perform Basic Set Operations
s1 = {1, 2, 3, 4, 5}
print('Original Set:', s1)  
s1.add(6)
print('Set after adding 6:', s1)
s1.remove(3)
print('Set after removing 3:', s1)
s1.update({7, 8})
print('Set after updating with {7, 8}:', s1)

#Exercise 2: Union of Sets
s2 = {1, 2, 3}
s3 = {3, 4, 5}
union_set = s2.union(s3)
print('Union of sets:', union_set)

#Exercise 3: Intersection of Sets
s4 = {1, 2, 3}
s5 = {2, 3, 4}
intersection_set = s4.intersection(s5)
print('Intersection of sets:', intersection_set)

#Exercise 4: Difference of Sets
s6 = {1, 2, 3}
s7 = {2, 3, 4}
difference_set = s6.difference(s7)
print('Difference of sets:', difference_set)

#Exercise 5: Symmetric Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)

print(result)

#Exercise 6: Add a list of Elements to a Set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

for item in sample_list:
    sample_set.add(item)

print(sample_set)

#Exercise 7: Set Difference Update
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)

print(set1)

#Exercise 8: Remove Items From Set Simultaneously

sample_set = {10, 20, 30, 40, 50}
items_to_remove = {10, 20, 30}

sample_set.difference_update(items_to_remove)

print(sample_set)

#Exercise 9: Check Subset
set1 = {10, 20, 30}
set2 = {10, 20, 30, 40, 50}

print(set1.issubset(set2))

#Exercise 10: Check Superset
set1 = {10, 20, 30, 40, 50}
set2 = {10, 20, 30}

print(set1.issuperset(set2))

#Exercise 11: Set Intersection Check
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print(set1.isdisjoint(set2))

#Exercise 12: Set Symmetric Difference Update
et1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

set1.symmetric_difference_update(set2)

print(set1)

#Exercise 13: Set Intersection Update
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

set1.intersection_update(set2)

print(set1)

#Exercise 14: Find Common Elements in Two Lists
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

result = []

for item in list1:
    if item in list2:
        result.append(item)

print(result)

#Exercise 15: Frozen Set
sample_set = {"apple", "banana", "mango"}

frozen = frozenset(sample_set)

print(frozen)

#Exercise 16: Count Unique Words
words = ["apple", "banana", "apple", "orange", "banana", "grape"]

unique_words = set(words)

print("Unique words:", unique_words)
print("Count:", len(unique_words))