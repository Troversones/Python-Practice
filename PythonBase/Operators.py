x = 15
y = 4

print("Aritmetic operators")
print(x + y)
print(x - y)
print(x * y)
print(x / y) #Div
print(x % y) #Modulus
print(x ** y) #Exponentiation
print(x // y) #Floor div

print("Assignment operators (some of them)")
print(" &= is primarily used to update intersections of built in set types")
a = set('abc')
a &= set('cbe') # same as a.__iand__(set('cbe'))
#what I did here was perform an 'AND' operation on two sets and put the same elements the 'intersected' with each other into 'a'
print(a)
print("The opposite can be done with the |= assignment operator")
print("bitwise XOR")
x = 5      # binary: 101
x ^= 3     # binary: 011
'''
simply put:
101
011
---
110
'''
print(x) #and this should be: 6

print("right shift: >>= and left shift: <<=")
#Shift bits to left or right
x = 16      # binary: 10000
x >>= 2     #shift right by 2
print(x) # in this case the binary moved: 10000 -> 01000 -> 00100 with 2 iterations and this should be 4

#same shi(f)t the left
x = 3       # binary: 11
x <<= 2
print(x) # and magically it turns into 01100 = 12

print(" \"Walrus\" operator := which basically it assigns value and returns at the same time")
print(x := 3)