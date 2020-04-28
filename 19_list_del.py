names = ['milu', 'Misan', 'millan', 'Babloo', 'anil']
print(names)
print("When you delete an item by its position in the list,"
"the items that follow it move back to take the deleted"
"item’s space, and the list’s length decreases by one."
"If we delete 'Harpo' from the last version of the"
"marxes list, we get this as a result:")
del names[3]
print(names)
"""del is a Python statement, not a list method—you
don’t say marxes[-2].del(). It’s sort of the reverse
of assignment (=): it detaches a name from a
Python object and can free up the object’s
memory if that name was the last reference to it."""