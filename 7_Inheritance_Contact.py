class Contact:
    all_contacts =[]

    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class  Supplier(Contact):
        def order(self,order):
            print("If this were a real system we would send "
                  "'{}' order to '{}' ".format(order,self.name))


c =Contact("milu","meet2millan@gmail.com")
s =Supplier("millan","meet2milu@gmail.com")
print(c.name,c.email,s.name,s.email)
print(c.all_contacts)
#c.order("I need a Brsuh")
s.order("I need a Brush")
print(s.order)