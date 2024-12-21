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

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if contact in self.contacts:
            print(f"Duplicate contact found: {contact}")
        else:
            self.contacts.append(contact)
            print(f"Contact added: {contact}")


if __name__ == "__main__":
    print("UC6: Prevent Duplicate Entries")
    address_book = AddressBook()

    contact1 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    contact2 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)  # This should identify a duplicate
