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

    def delete_contact(self, first_name, last_name):
        self.contacts = [contact for contact in self.contacts if not (contact.first_name == first_name and contact.last_name == last_name)]
        print(f"Contact {first_name} {last_name} deleted.")


if __name__ == "__main__":
    print("UC3: Delete a Contact")
    address_book = AddressBook()
    contact = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    address_book.add_contact(contact)
    address_book.delete_contact("John", "Doe")
