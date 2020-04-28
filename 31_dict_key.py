dictionary = {'Name': 'Millan Kumar Das', 'Age': '20', 'color': 'Black', 'class': 12}
print(dictionary.keys())
print("to convert all keys into list :")
_list = list(dictionary.keys())
print(_list)
print("To get all values : ")
print(list(dictionary.values()))
print("Get all key-value pairs by using items()")
print(list(dictionary.items()))
print("each key and value is returned as a tuple, such as ('age','20')")

print("Copy or assign with  = ")
new_dictionary = dictionary
print("New dictionary is : ")
print(new_dictionary)

original_dict = new_dictionary.copy()
print(original_dict)


print('Name' in new_dictionary)
print(new_dictionary['Name'])
original_dict.clear()
print(original_dict)


