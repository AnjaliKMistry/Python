# 1. Take two numbers and perform all arithmetic operations
a = 10
b = 2
print("Task-1")
print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Floor division: ",a//b)
print("Modulus(remainder): ",a%b)
print("Power: ",a**b)

# 2. use every assignment operator once.
print("Task-2")
c = 3
print(c)
c += 1
print(c)
d = 4
d -= 2
print(d)
e = 7
e *= 2
print(e)
f = 8
f /= 3
print(f)
g = 9
g //= 4
print(g)
h = 22
h %= 3
print(h)
i = 3
i **= 2
print(i)

# 3. check whether a number is even or off
print("Task-3")
num = int(input("Enter a number: "))
if (num%2==0):
    print("Even")
else:
    print("Odd")

# 4. check whether a character exists in a string
print("Task-4")
string = input("Enter a string: ")
character = input("Enter a character: ")
if character in string:
    print(f"{character} is present in given string")
else:
    print(f"{character} is not present in given string")

# 5. compare two numbers
print("Task-5")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)

# 6. find largest of two numbers
print("Task-6")
n1 = int(input("Enter num 1: "))
n2 = int(input("Enter num 2: "))
if (n1>n2):
    print("Largest is: ",n1)
else:
    print("Largest is: ",n2)

# 7. demonstrate all bitwise operators using 5 and 3
print("Task-7")
x = 5
y = 3
print("and operation: ", x&y) # 1
print("or operation: ",x|y) # 7
print("not operation: ",~x) # -6
print("xor operation: ",x^y) # 6
print("left shift: ",x<<y) # 40
print("right shift: ",x>>y) # 0

# 8. calculate square, cube and power
print("Task-8")
n = int(input("Enter a number: "))
p = int(input("Enter power: "))
print(f"Square of {n} is ",n**2)
print(f"Cube of {n} is ",n**3)
print(f"Power of {n} is ",n**p)

# 9. show operator precedence using different expressions
print("Task-9")
print(2+5*6) # priority *>+
print((5-1)/2+1) # priority ()>/>+
print(5-(2*2)) # priority ()>*>-

# 10. create a mini calculator
print("Task-10")
a1 = int(input("Enter number 1: "))
op = input("Enter operator like +,-,*,/,%,**")
a2 = int(input("Enter number 2: "))
if op=="+":
    print("Addition is: ",a1+a2)
elif op=="-":
    print("Subtraction is: ",a1-a2)
elif op=="*":
    print("Multiplication is: ",a1*a2)
elif op=="/":
    print("Division is: ",a1/a2)
elif op=="%":
    print("Modulus(remaider) is ",a1%a2)
elif op=="**":
    print("Square of it is: ",a1**a2)
else:
    print("Invalid opeartor")