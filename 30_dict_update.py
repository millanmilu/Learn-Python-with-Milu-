_dict ={'Name': 'Millan Kumar Das', 'Age': '20', 'color': 'Black'}
other = { 'class': 12}

print("first dict ")
print(_dict)
print("print second dict ")
print(other)
print("Now update two ")
_dict.update(other)
print(_dict)

print("use to del key")
del _dict['class']
print(_dict)

print("Delete all item by clear()")
_dict.clear()
print(_dict)