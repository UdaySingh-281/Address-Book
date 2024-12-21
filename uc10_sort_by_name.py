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
        return f"{self.first_name} {self.last_name}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def sort_by_name(self):
        return sorted(self.contacts, key=lambda c: (c.first_name, c.last_name))


if __name__ == "__main__":
    print("UC10: Sort Contacts Alphabetically by Name")
    address_book = AddressBook()

    contact1 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    contact2 = Contact("Alice", "Brown", "789 Pine St", "Springfield", "IL", "62701", "555-6789", "alice.brown@example.com")
    contact3 = Contact("Jane", "Smith", "456 Oak St", "Chicago", "IL", "60601", "555-5678", "jane.smith@example.com")

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    address_book.add_contact(contact3)

    sorted_contacts = address_book.sort_by_name()
    print("Sorted contacts by name:", [str(contact) for contact in sorted_contacts])
