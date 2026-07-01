# Taking Input
# input() --> used to take input from the user

# name = input("Enter your name: ")
# print(name)

# input() --> always returns a string
num = input("Enter a number: ")
print(type(num)) # <class 'str'>

### Type Conversion

## 1. int() --> converts data to integer
# num = int(input("Enter number: "))

## 2. float() --> converts data to float
# price = float(input("Enter price: "))

## 3. str() --> converts data to string
age = 20
print(type(str(age)))

### f-Strings --> used to format string
name = "anjali"
print(f"my name is {name}")

# Input :- Input means data entered by the user. The user gives information to the program
# Output :- Output means the result shown by the program

# Output using print()
# print() is a built-in python function used to display output.
# print multiple values 
name = "anjali"
age = 20
print(name,age)

"""Input using input()
input() is a built-in python function that accepts input from the user
input() always returns a string"""

# Multiple inputs in one line
name1,age1=input("Enter name and age: ").split()
print(name1,age1)

# Taking multiple integers
