class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"
class Contact_Book:
    def __init__(self):
        self.contacts = {}
    
    def add_contacts(self, contact):
        if contact.name in self.contacts:
            print(f"'{contact.name}' already exists.")
        else:
            self.contacts[contact.name] = contact
            print(f"Contact added successfully")
    def view_contacts(self):
        if not self.contacts:
            print("No contacts have been added")
        else:
            for contact in self.contacts.values():
                print(contact)
    def search_contacts(self, target):
        for contact in self.contacts.values():
            if target.lower() in contact.name.lower():
                return contact
        for contact in self.contacts.values():
            if target in contact.phone:
                return contact
            
        return f"'{target}' not found"
    def update_contact(self, name, updated_name = None, phone = None, email = None, address = None):
        if name in self.contacts:
            contact = self.contacts[name]
            if updated_name:
                contact.name = updated_name
            if phone:
                contact.phone = phone
            if email:
                contact.email = email   
            if address:
                contact.address = address
            print(f"Contact updated successfully")
        else:
            print(f"Contact not found. Try again")         

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact deleted successfully")
        else:
            print(f"Contact not found.")

def main():
    contact_book = Contact_Book()
    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. View contact list")
        print("3. Search for a contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address:")
            contact = Contact(name, phone, email, address)
            contact_book.add_contacts(contact)
        if choice == '2':
            print ("\nAll Contacts:")
            contact_book.view_contacts()
        if choice == '3':
            target = input("Enter contact name or number: ")
            result = contact_book.search_contacts(target)
            print (result)
        elif choice == '4':
            name = input("Enter name of contact you want to update: ")
            updated_name = input("Enter updated name or skip: ")
            phone = input("Enter updated phone number or skip: ")
            email = input("Enter updated email address or skip: ")
            address = input("Enter updated address or skip: ")
            contact_book.update_contact(name, updated_name if updated_name else None, phone if phone else None, email if email else None, address if address else None)
        elif choice == '5':
            name = input("Enter contact name you want to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
I've just completed my fifth task at Codsoft – building a Contact Book Application in Python. The application allows users to manage their contacts efficiently, and includes features such as adding, viewing, searching, updating, and deleting contacts.



Through this project, I learned the importance of creating intuitive, user-friendly interfaces and managing data effectively using Python's data structures like dictionaries.. This project deepened my understanding of object-oriented programming and reinforced the value of designing flexible and maintainable code. I also learned the difference between CamelCase and snake case and how to use them effectively.



Working on all these tasks taught me something new and I'm grateful for the opportunity to work with CodSoft

#Python #Programming #Coding #PythonProjects #DataManagement #OOP #SoftwareDevelopment #ContactBook #Codsoft