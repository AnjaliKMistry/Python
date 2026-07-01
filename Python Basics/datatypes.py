# A datatype tells python what kind of value is stored in a variable
# every value in python has datatype
# Python has different datatypes

# 1. Integer (int)
age = 20 # stores whole numbers

# 2. Float
price = 99.99 # stores decimal numbers

# 3. String (str)
name = "anjali" # stores text

# 4. Boolean (bool)
is_student = True # stores True or False

## Checking Data Type

# type() --> used to find the data type of a value
x = 10
print(type(x)) # <class 'int'>

a = "anjali"
print(type(a)) # <class 'str'>

b = 1.2
print(type(b)) # <class 'float'>

c = True
print(type(c)) # <class 'bool'>

print(type(False)) # <class 'bool'>

"""Built in Data Types in Python
Numeric--> int, float, complex
Boolean--> bool
Text--> str
Sequence--> list, tuple, range
Set--> set, frozenset
Mapping--> dict
Binary--> bytes, bytearray, memoryview
Special--> NoneType"""

"""Numeric Data Types
1. int (Integer)
An integer is a whole number
it has no decimal point
2. float
A float is a number containing a decimal point
3. complex
complex number contain Real Part + Imaginary Part
It is used in Electrical Engineering, Signal Processing, Scientific Computing, Advanced Mathematics"""
number = 2 + 3j
print(number)
print(type(number))

"""Boolean Data Type (bool)
It has only two values.
True / False"""

"""None Data Type
None means No value or Nothing"""

"""Checking Data Types
python provides the type() function"""

"""What is id()
every object in python has an identity (ID)
The id() function returns the unique identity of an object
"""
name="Anjali"
print(id(name))
a=220.5
print(id(a))

"""Memory concept
when you write age=20 python creates an integer object in memory
now marks=age
both variables refer to the same object until one of them changes"""
age1=20
marks1=age
print(id(age1))
print(id(marks1))

"""Rules and important points
Every value has a data type
Python automatically detects the data type
True and False must start with capital letters
None starts with a capital N
Use type() to check a variables type
id() returns an object's identity in memory
Integers have no decimal point
Floats always contain a decimal point
Complex numbers use j, not i"""

"""String
A string is a collection(sequence) of characters enclosed in quotes
A string is used to store text
Everything inside quotes is a string"""
# using double quotes
name="Anjali"
# Using single quotes
city='surat'

"""List (list)
A list is an ordered collection of items
Lists can store Numbers, Strings, Boolean values, Even other lists
Lists are written using square brackets []
Mutable"""
fruits = ["Apple", "Banana", "Mango"]
numbers = [10,20,20]
print(numbers)
# Mixed Data Types
data = ["Anjali", 20, True, 8.5]
print(data)

"""Tuple (tuple)
A tuple is an ordered collection of items that cannot be changed after creation
Tuples use parentheses ()
Immutable"""
colors = ("Red", "Green", "Blue")
print(colors)

"""Set (set)
A set is an unordered collection of unique items
Sets use curly braces {}"""
nums = {10,20,30,30}
print(nums) # order may vary and duplicate values are removed automatically

"""Dictionary (dict)
A dictionary stores data in key-value pairs
Dictionary keys should be unique"""
student = {
    "name": "Anjali",
    "age": 20
}
print(student)

"""Range (range)
range() generates a sequence of numbers"""
nums1 = range(5)
print(nums1) # range(0, 5)
# converts to a list
print(list(nums1))

"""Bytes (bytes)
bytes stores binary data"""
data1 = b"Hello"
print(data1)

"""Bytearray (bytearray)
bytearray is similar to bytes, but it can be modified"""
data2 = bytearray([65, 66, 67])
print(data2)

"""Memoryview (memoryview)
A memoryview lets you access binary data without copying it"""
data3 = memoryview(bytes([65, 66, 67]))
print(data3)

"""Mutable vs Immutable
Mutable:- Mutable means can be changed after creation
--> List, Dictionary, Set, Bytearray
Immutable:- Immutable means cannot be changed after creation
--> int, float, bool, string, tuple, bytes"""
name="Anjali"
name="Rahul"
print(name)
# The original string "Anjali" did not change. Python created a new string object "Rahul" and made name refer to it.

"""Type Conversion (Type Casting)
Type Conversion means changing the data type of a valur from one type to another.
Types of Type Conversion
1. Implicit Type Conversion
Implicit means Python automatically converts one data type into another
2. Explicit Type Conversion
Explicit means the programmer converts the data type manually
Built-in Type Conversion Functions
int() :- converts a value into an integer
float() :- converts a value into a float
str() :- converts any value into a string
bool() :- converts a value into Boolean
list() :- converts another iterable into a list
tuple() :- converts into a tuple
set() :- converts into a set
dict() :- creates a dictionary from key-value pairs"""
# Implicit Type conversion
x=10
y=2.5
result=x+y
print(result)
print(type(result))
print(10+True) # 11
p=True
print(float(p)) # 1.0

"""False values
0, 0.0, "", [], {}, None"""

text = "Python"
print(list(text)) # ['P', 'y', 't', 'h', 'o', 'n']

numbers1 = [1,2,3]
print(tuple(numbers1)) # (1,2,3)
numbers2 = [1,2,3,4,2,3]
print(set(numbers2)) # {1,2,3,4} duplicate values are removed

data4 = [("name","anjali"),("age",20)]
print(dict(data4)) # {'name':'anjali','age':20}

data5 = (["name","vikas"],["age",23])
print(dict(data5)) # {'name': 'vikas', 'age': 23}

# Safe conversions
# It means python can perform the conversion without error
int("20")
float("10.3")
str(50)

# Unsafe conversion:- these conversions produce errors
# int("Hello") # ValueError
# int("10.5") # ValueError 

# Practice Programs

# 1. Convert "100" into an integer
print("Task-1")
a1 = "100"
a1=int(a1)
print(type(a1))

# 2. Convert 50 into a float.
print("Task-2")
a2 = 50
a2 = float(a2)
print(type(a2))

# 3. Convert 25 into a string
print("Task-3")
a3 = 25
a3 = str(a3)
print(type(a3))

# 4. Print the type before and after conversion
print("Task-4")
a4 = 23
print(type(a4))
a4 = float(a4)
print(type(a4))

# 5. Convert a tuple into a list.
print("Task-5")
a5 = (1,2,3,"Hello",5.6)
a5 = list(a5)
print(a5)

# 6. Convert a list with duplicate values into a set.
print("Task-6")
a6 = [1,2,3,"Hello","Hello",44,56,2.2,1,2,3,3,7]
a6 = set(a6)
print(a6)

# 7. Convert a list of key-value pairs into a dictionary
print("Task-7")
a7 = [["Name","Kavya"],["Rollno",45]]
a7 = dict(a7)
print(a7)

# 8. Create variables of different data types and convert each one into another suitable type
b1 = 10
b2 = 10.6
b3 = "abcs"
b4 = True
b5 = [1,2,3,4,5,1]
b6 = (1,2,4,4,99)
b7 = {1,2,3,4,5,90,1}
b8 = {"name":"anjali","age":22}

print(float(b1)) # 10.0
print(str(b1)) # 10
print(bool(b1)) # True
# print(list(b1)) --> int object is not iterable
# print(tuple(b1)) --> int object is not iterable
# print(set(b1)) --> int object is not iterable
# print(dict(b1)) --> int object is not iterable