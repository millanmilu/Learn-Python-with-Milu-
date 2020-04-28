"""A set is like a dictionary with its values thrown
away, leaving only the keys. As with a dictionary,
each key must be unique. You use a set when you
only want to know that something exists, and nothing
else about it. Use a dictionary if you want to attach
some information to the key as a value.
"""
list= [1,2,3,4]
print("Create a set ")
even_numbers = {0,2,4,6,8}
odd_numbers = {1,3,5,7,9,}
print(odd_numbers,even_numbers)
new = set(list)
print(new)
new.add(" New")
print(new)
#print(new.remove("new"))
print(new)
new.discard("new")
new.pop()
del new
set3 = even_numbers.union(odd_numbers)

print(set3)