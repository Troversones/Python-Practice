import sys
import random

#comment
print(sys.version)
print("How many energy drinks you drink a day?")
"""
also a comment
"""

#Variables
x = 5 # type conversion happens and the variable switches to str
x = "5"
y = ", is that a lot?"
print(x, end="") #end continues to the next print without breaking the line, only applies to 1 more print statement
print(y)
print(type(x)) #type check

#type casting
"""
x = str(3) == '3'
x = int(3) == 3
x = float(3) == 3.0
"""

#Variable declaration rules
"""
Case-sensitive (As, AS, as are 3 different variables) 
Starting letter must be a letter or an underscore character
Cannot start with a number
Cannot be split be e.g. whitespace
Can only contain alpha numeric characters
Cannot be any python keywords
"""

#Multi word variable name best practices (choose at your own leisure)
"""
Camel Case:
    myVariableName = 0
Pascal Case:
    MyVariableName = 0
Snake Case:
    my_variable_name = 0
"""

#Multi value assignment

#Assigning multiple variables to multiple values in order
x, y, z = 1, 2 ,3
print(x, end= " ")
print(y, end=" ")
print(z)
#Assign multiple variables to one value
x = y = z = 1
print(x, end=" ")
print(y, end=" ")
print(z)

#Unpack a collection
collection = ["first", "second", "third"]
x, y, z = collection
print(x, end=" ")
print(y, end=" ")
print(z)
#printing multiple values is just '+' them together, but for numbers it is a mathematical operator
#if given a number and a string you want to print out don't use '+' rahter split them with ','

#Global variables (I declared most of the previous values globally)
def random_func():
    x = "Testing the function" #giving new value to x is going to stay in this scope
    print(x) #for example x can be reached from anywhere
    global t
    t = "global test" #but of course you can declare a global scope variable inside a function XD

random_func()
print(x, end=" ") #should be "one"
print(t)

#Random and complex data type
x = 2+3j
print(type(x))
x = random.randrange(1,1024)
print(x)

#Boolean segment
'''
Empty values are false
boolean segment over kek
'''

