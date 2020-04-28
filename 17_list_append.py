names= ['milu','millan','anil']
other_names = [ "Gummo","Karl"]

print("The append() function adds items only to the end of the list")
names.append('Zeppo')
print(names)
print("You can merge one list into another by using extend")
names.extend(other_names)
print(names)

print("Alternatively, you can use +=:")
names += other_names
print(names)