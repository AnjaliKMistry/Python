# 1. swap two numbers without third variable
# print("Task-1")
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# a = a + b
# b = a - b
# a = a - b
# print("a = ",a)
# print("b = ",b)

# 2. find greatest among three numbers.
# print("Task-2")
# n1 = int(input("Enter num 1: "))
# n2 = int(input("Enter num 2: "))
# n3 = int(input("Enter num 3: "))
# if n1>n2:
#     if n1>n3:
#         print(f"{n1} is greatest number")
#     else:
#         print(f"{n3} is greatest number")
# else:
#     if n2>n3:
#         print(f"{n2} is greatest number")
#     else:
#         print(f"{n3} is greatest number")

# 3. convert celsius to fahrenheit
# print("Task-3")
# C = float(input("Enter temperature Celsius: "))
# F = (9/5)*C + 32
# print("Temperature in Fahrenheit = ",F)

# 4. check if a year is leap year. 
# a year is leap year if it is divisible by 400 or divisible by 4 and not divisible by 100
print("Task-4")
year = int(input("Enter year: "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

# 5. create a scientific calculator using operators
print("Task-5")
# already done in practice