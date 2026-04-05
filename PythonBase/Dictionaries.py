'''
DICTIONARIES

Ordered data structure,
does NOT allows duplicates
and stores values in [key:value] pairs

the method below is how you create one but just like in previous data structures it can be
called with It's contructor dict()

for example:
somedict = dict(name="Someone",age=34,country="Sweden")

a value inside a dictionary can be all data types e.g.: string,int,tuple,list etc.

type is <class 'dict'>
'''

testdict = {
    "name" : "Jonathan Joestar",
    "age" : 18,
    "muscles" : True
}
print(testdict) 
print(testdict["age"]) # This can be put into a variable
#using the .get() is kinda the same as calling it directly
testvar = testdict.get("age")
print(testvar)
#the .keys() on the other hand returns all the key entries present in the dictionary
keysTestVar = testdict.keys()
print(keysTestVar)

#we can add more key entries to it
testdict["newkey"] = "new"
print(testdict)

#We can get all the values of the dict with the .values() function
print(testdict.values())

#but if we change the age for example, not a new entry but the value of a single element is going to change
testdict["age"] = 20
print(testdict)

'''
The .items() method will return each item in dictionary, as TUPLES in a list
for example:
    dict_items([('name', 'someName'), ('age', 20), ('moustache', True)])
'''

print(testdict.items())

#Check if a key exists
if "something" not in testdict:
    print(False)

#Changing items if the argument does not exists in the dict it will be added to it instead
testdict.update({"newkey": "old"})
print(testdict)

'''
Removing items
    somedict.pop("keyName") - remove item with specified key name
    somedict.popitem() - removes last inserted item
    del somedict["keyName"] - remove item with specified key name

    or just delete it completely via. - del somedict or clear it with .clear()
'''

'''
#Looping via key name
for x in testdict:
    print(x)

#print via values
for x in testdict:
    print(testdict[x])

#or use this instead iterating through the values itself
for x in testdict.values():
    print(x)

or use .keys()

or .items() which allows us to iterate through both value and keys
for x, y in testdict.items():
    print(x, y)
    
'''
#making a copy
newCopy = testdict.copy()
print(testdict)

#Nested dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#and for example print the name of child2 
print(myfamily["child2"]["name"])
'''
Example for loop:
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

Dictionary methods: https://www.w3schools.com/python/python_dictionaries_methods.asp
'''