someList = ['one','two','three']
print(someList) #basic list print
'''
ORDERED AND CHANGABLE collection

Lists 'allow duplicates'

Items can be indexed via []
len() function very cool indeed

Lists can contain any data type and can hold up more data types at the same time
e.g.: list = [42,'string',True]
<class 'list'> type
can be called via list() contructor
'''

listCallContruct = list(('some','list','expand','a','bit','more'))
print(listCallContruct)

'''
Indexing / accessing items
[-1] Last item [-2] second to last - basically indexing backwards

[2:5] indexing from 2-5 which returns a new sliced list, NOTE: this does not include the last indexed element

[:4] this does the same but if we don't specify a starting range It's gonna go from the start '0' and not include the fifth element

[4:] can be done the same way but this time the last indexed element won't be cut out
'''
print("Negative indexes work the same way, the latter is going to be the end")
print("in this example -1 (more) is not going to be included")
print(listCallContruct[-4:-1])

if 'bit' in listCallContruct : #can be called on lists if something is in the list
    print("That's indeed a small 'bit' don't you think?")

'''
Change list items via indexing someList[0] = '1'
Inserting a range of items
    [1:3] and [1:2] for example should insert 2 and 1 items each in order
    now let's see an example of that
'''
print("Inserting elements")
listCallContruct[0:2] = ["do", "you"]
print(listCallContruct)
#But if we were to insert more than we indexed
listCallContruct[1:2] = [listCallContruct[1],"think","you","can"]
print(listCallContruct) #Then it inserts the remaining elements from that point onwards

print("Inserting from a certain index: brought to you by yours truly - .insert()")
listCallContruct.insert(9, "?")
print(listCallContruct)

#Inserting list items via append, or insert just like I used in the previous example (inserting at the end of the list)
listCallContruct.append("?")
print(listCallContruct)
#remove elements via .remove (removes first occurence)
listCallContruct.remove("?")
print(listCallContruct)
#remove via .pop which removes a certain index
listCallContruct.pop(0)
print(listCallContruct)
#del can remove a certain index or the entire list completely this way if you choose to do so the list cannot be invoked from that point on
del listCallContruct[0]
print(listCallContruct)

#and lastly clear which clears the whole list but the list remains so we can add more elements to it later
listCallContruct.clear()
print(listCallContruct)
del listCallContruct

#Loops
testList = [1,2,3,4,5,6,7,8,9,10]
for i in testList: #or loop through the index via for i in range(len(testList)): print(testList[i])
    print(i, end=" ")

j = 0
while j < len(testList):
    print(testList[j], end=" ")
    j += 1
#or a short hand loop
[print(x, end=" ") for x in testList]

'''
List comprehension rule NOTE: newlist = [expression for item in iterable if condition == True]
'''
newList = [x**2 for x in testList]
print(newList)

#Sorting lists  alphanumerically, ascending, by default:
sortThis = [100,50,24,3,44,1,23,153]
sortThis.sort()
print(sortThis)
sortThis.sort(reverse=True)
print(sortThis)

'''
Sort the list based on how close the number is to 50 - NOTE: we can use a key to define a customized function to a sort

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

NOTE: by default sort() is case sensitive resulting in all capital letters being sorted before lower case letters
So if you want a case-insensitive sort function, use str.lower as a key function

for example:
someList.sort(key = str.lower) 

'''
#pretty self explanetory 
sortThis.reverse()
print(sortThis)

#copy lists
newSortThis = sortThis.copy() #or another way to make a copy is the list(someList) contructor
print(newSortThis)
#or if you feel really fancy with the slice operator newSortThis = sortThis[:]

'''
Joining lists
list3 = list1 + list2 NOTE: this creates a new list

or

for x in list2:
  list1.append(x)

or

list1.extend(list2)

take your pick
'''

#Methods
'''
Take your pick

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''