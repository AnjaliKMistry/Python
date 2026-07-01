# A variable is a name used to store data
name = "Anjali" # name--> variable and Anjali--> value
age = 20 # age--> variable and 20--> value

# Rules for naming variables
# valid variable names
name = "Anjali"
student_name = "anjali"
age1 = 20

# Multiple assignment
a,b,c=10,20,30 # correct
# same value to multiple varibale
x=y=z=100

# Invalid variable names
# 1name = "Anjali" --> does not start with numbers
# my-name = "Anjali" --> does not use any symbol only use _
# class = 10 --> does not start with any keywords

# keywords
import keyword
print(keyword.kwlist)

# swapping variables
i=20
j=40
i,j=j,i
print(i,j)

# deleting variable
# del keyword 