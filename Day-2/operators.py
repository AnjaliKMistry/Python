# An operator is a symbol that performs an operation on one or more operands.
# a = 10
# b = 5
# print(a+b) # + is an operator & a,b are operands

"""1. Arithmetic Operators
--> + , Addition (10+5)
--> - , Subtraction (10-5)
--> * , Multiplication (10*5)
--> / , Division (10/5)
--> // , Floor Divison (10//3)
--> % , Modulus (10%3)
--> ** , Power (2**3)"""
print("Arithmetic Operators")
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b) # Returns a remainder
print(a**b)

# % operator is important for even/odd numbers, pattern problems, logic building

"""2. Comparison Operators
== --> Equal
!= --> Not Equal
> --> Greater Than
< --> Less than
>= --> greater than or equal
<= --> less than or equal"""
print("Comparison Operators")
c = 10
d = 20
print(c==d)
print(c!=d)
print(c>d)
print(c<d)
print(c>=d)
print(c<=d)

"""3. Assignment Operator (used to assign values)
Simple assignment (=)
Add and assign (+=)
Subtract and assign (-=)
Multiply and assign (*=)
Divide and assign (/=)
Floor Divide and assign (//=)
Modulus and assign (%=)
power and assign (**=)
"""
"""4. Logical Operator 
AND --> returns true if both conditions are true
OR --> returns true if atleast one condition is true
NOT --> reverse the result"""
print("Logical Operator ")
print(True and False)
print(True or False)
print(not True)
print(3 and 5)
print(3 or -6)
print(not 7)
print(10 and 6)
print(17 or 2)

"""5. Bitwise Operators (computer stores data in binary)"""
print("Bitwise Operators")
# Bitwise and (&)
print(5 & 2)
# Bitwise or (|)
print(5 | 2)
# Bitwise xor (^)
print(5^2)
# Bitwise not (~) --> ~n = -(n+1)
print(~5)
# left shift (<<) (rule:- n<<k = n* 2^k)
print(5<<1)
# right shift (>>) (rule:- n>>k = n/2^k)
print(8>>1) 

"""6. Membership Operators (used with strings, lists, tuples, sets)"""
print("Membership Operators")
# in
name = "python"
print("p" in name)
print("k" in name)
# print(3 in name) # error

# not in
name1 = "anjali"
print("a" not in name1)
print("f" not in name1)
# print(5 not in name1) # error

"""7. Identity Operators (checks whether two variables refer to the same object)"""
print("Identity Operators")
# is
i = [1,2]
j = i
print(i is j)
# is not
print(i is not j)

"""Operator Precedence (order in which operators are executed)
precedence order
()
**
*,/,//,%
+,-
Comparison
not
and
or
"""