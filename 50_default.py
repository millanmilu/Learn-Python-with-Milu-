i = 5
def f (arg = i ):
	print(arg)
i = 6
f()	

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return print(L)
f(1)