# Taking Input
# input() --> used to take input from the user

# name = input("Enter your name: ")
# print(name)

# input() --> always returns a string
num = input("Enter a number: ")
print(type(num)) # <class 'str'>

### Type Conversion

## 1. int() --> converts data to integer
num = int(input("Enter number: "))

## 2. float() --> converts data to float
price = float(input("Enter price: "))

## 3. str() --> converts data to string
age = 20
print(type(str(age)))

### f-Strings --> used to format string
name = "anjali"
print(f"my name is {name}")