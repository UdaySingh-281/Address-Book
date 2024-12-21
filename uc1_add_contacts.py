# uc1_add_contact.py
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
        if contact in self.contacts:
            print(f"Duplicate contact found: {contact}")
        else:
            self.contacts.append(contact)
            print(f"Contact added: {contact}")


# Main function to test UC1
if __name__ == "__main__":
    print("UC1: Add a New Contact")

    # Create an AddressBook instance
    address_book = AddressBook()

    # Add a new contact
    contact = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    address_book.add_contact(contact)

    # Add another contact
    another_contact = Contact("Jane", "Smith", "456 Oak St", "Chicago", "IL", "60601", "555-5678", "jane.smith@example.com")
    address_book.add_contact(another_contact)
