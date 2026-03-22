'''
Tuples are immutable (or unchangeable if someone likes that more)

I'm not gonna detail pretty much anything here because It's the same as lists to be fair

NOTE: only one noteworthy thing to mention is that altough it is an immutable data structure there's a workaround

Convert it into a list then change what you want the convert back XD

x = ("some", "things", "don't","change")
y = list(x)
y[2] = "can"
x = tuple(y)

print(x)

OR

add tuple to tuple
thistuple = ("is", "this", "any","better","?")
y = ("?",) don't forget to add the comma here otherwise it doesn't identify as a tuple(as funny as that might sound in 2026)
thistuple += y

removing is the same
'''