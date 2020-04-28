class Addition:
    def add(self,a=None,b=None,c=None):
        s =0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s =a
        return s
a =Addition()
print(a.add(10,10,1))

