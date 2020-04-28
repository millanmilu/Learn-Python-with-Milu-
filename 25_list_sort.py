names = ['milu', 'Misan', 'millan', 'Babloo', 'anil']
print("sorted by"
"default in ascending numeric order. If they’re strings,"
"they’re sorted in alphabetical order")
sorted_names = sorted(names)
print(sorted_names)
print("sorted_names is copy ,didn't change the original,calling the list function sort() on the names list")
names.sort()
print(names)

numbers  = [2,1,4,0,3,5.5]
numbers.sort()
print(numbers)
print("for descending order type reverse = True")
numbers.sort(reverse= True)
print(numbers)

