class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email


class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)


class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        if name in self.address_books:
            print(f"Address book '{name}' already exists.")
        else:
            self.address_books[name] = AddressBook(name)
            print(f"Address book '{name}' created.")


if __name__ == "__main__":
    print("UC5: Manage Multiple Address Books")
    system = AddressBookSystem()
    
    while True:
        name = input("Enter Address Book Name: ")
        system.add_address_book(name)
        more = input("Add another address book? (yes/no): ")
        if more.lower() != "yes":
            break
