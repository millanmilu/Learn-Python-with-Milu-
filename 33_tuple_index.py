thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:3])
print(thistuple[2:6:2])

for x in thistuple :
    print(x)

if "apple"  in thistuple:
    print("yes")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

print(thistuple.count("apple"))
print(thistuple.index("apple"))

