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

print("comparison operators are just very basic so I'm skipping those I know anyway")

print("Logical operators: 'and' 'or' 'not' which basically is &,| or ! respectively")

print("Identity op: (is , is not) very simple ye?")
'''
Membership op: in, not in
'''

print("Bitwise operators:")
'''
& - 'AND' : Sets each bit to 1 if both bits are 1
| - 'OR' : Sets each bit to 1 if one of two bits is 1
^ - 'XOR' : Sets each bit to 1 if only one of two bits is 1
~ - 'NOT' : Inverts all the bits
<< - 'Zero fill left shift' : Shift left by pushing zeros in from the right and let the leftmost bits fall off
>> - 'Signed right shift' : Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
'''

print(6 & 3) #binaries: 0110 and 0011
#which prints out 2 since it becomes 0010

print(6 | 3) #this prints out 7 -> 0111

print(6 ^ 3) #this prints 5 -> 0101
#if both is 1 or 0 then it sets to 0

'''
might be worth to mention the Precendence order (top-bottom descending order by priority)
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
'''