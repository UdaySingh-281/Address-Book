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

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.city}, {self.state}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact added: {contact}")


if __name__ == "__main__":
    print("UC4: Add Multiple Contacts")
    address_book = AddressBook()

    while True:
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter Zip Code: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        address_book.add_contact(contact)

        more = input("Add another contact? (yes/no): ")
        if more.lower() != "yes":
            break
