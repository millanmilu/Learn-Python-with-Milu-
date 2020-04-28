class ContactList(list):
    def search(self,name):
        matching_contacts =[]
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
class Contact:
    all_contacts =ContactList()
    def __init__(self,name,email):
        self.name =name
        self.email = email
        self.all_contacts.append(self)
class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here
class EmailableContact(Contact, MailSender):
    pass
c1 = Contact("Milu 1","meet2millan@gmail.com")
c1 = Contact("Milan 2","meet2millan@gmail.com")
c1 = Contact("Millan 3","meet2millan@gmail.com")
print([c.name for c in Contact.all_contacts.search("Millan")])
e = EmailableContact("Milu 1", "jsmith@example.net")
e.send_mail("Hello")
print(Contact.all_contacts)
