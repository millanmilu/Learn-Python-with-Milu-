d = {'a':1,'b':2,'c':3}
print(d)

ks= list(d.keys())
print(ks)

ks.sort()


for key in ks:
	print(key,'=>',d[key])

for key in ks:
	print(key.upper())	