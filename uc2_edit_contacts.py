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
        return f"{self.first_name} {self.last_name}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, first_name, last_name, updated_contact):
        for i, contact in enumerate(self.contacts):
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts[i] = updated_contact
                print(f"Contact updated: {updated_contact}")
                return
        print("Contact not found.")


if __name__ == "__main__":
    print("UC2: Edit Existing Contact")
    address_book = AddressBook()
    contact = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    contact2 = Contact("Joe", "Doe", "123 Elm", "Springfield", "IL", "6271", "555-234", "joe.doe@example.com")
    address_book.add_contact(contact)
    address_book.add_contact(contact2)
    updated_contact = Contact("John", "Doe", "456 Maple St", "Chicago", "IL", "60601", "555-5678", "john.doe@example.com")
    address_book.edit_contact("John", "Doe", updated_contact)
    updated_contact = Contact("Jo", "Do", "456 St", "Chicago", "Indonesia", "60601", "555-5678", "jo.do@example.com")
    address_book.edit_contact("Joe", "Doe", updated_contact)
