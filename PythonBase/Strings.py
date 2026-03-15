print("can use 'quotes' as long as they don't match the quotes surrounding the string")
print('like "this" !')
#multi line comments can be printed with """multi line comm""" and with ''' ''' aswell
#printing certain characters in string can be done via indexing e.g. someString[0] first character of string

#loop through string
for x in "asd":
    print(x)

'''
#for length just use len()
#check if a certain string for example "asd" is present in the given string using and inline if statement print("asd" in someString)
#On the other side this works with 'not in' which is the opposite of this
'''
#Slicing strings
b = "Some String, maybe something tricky this time?"
print(b[5:15])#slice from range e.g. 5-15 in here 
print(b[:5])#slice from start -> value can do the same reversed [2:] - value to end

print(b[-17:-10]) #this type of indexing goes backwards just imagine -10 here is the starting char and -17 is the end
#Modify string - .lower .upper usual stuff 
#and remove white space (strictly before and after text)
print(("                 this could be huge         but It's not                     ").strip()) 
#split works just like always, give a splitter char like ',' and .split the string

#merge a with b into c
a = "Something"
b = "Nice"
c = a+" "+b
print(c)
#also if I add int to str it gives back an error "TypeError: must be str not int"
money = 2300.55
textForStringFormat1 = f"Someone could have {money:.3f} euros in his bank account" # with the 'f' we can put variables into string 
print(textForStringFormat1) #and with : after them make it a float number aswell

print("Trying to put \"something\" together?") # this is how to put quotes in a string
print("print 1 backslashes \\")#with 2 backslashes
'''
Backslash: \\
New line: \n
Carriage return?: \r
Tab: \t
Octal value: \123 or any 3 number really
Hex val: same just with hex after the \x43
''' 
#string methods (I'm not memorizing these)
#honestly just use them to your liking: https://www.w3schools.com/python/python_strings_methods.asp
