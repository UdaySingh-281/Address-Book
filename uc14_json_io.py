import json

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

    def to_dict(self):
        return self.__dict__


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
        print(f"Address book saved to {file_name}")

    def load_from_json(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                for contact in data:
                    print(contact)
        except FileNotFoundError:
            print(f"File {file_name} not found.")


if __name__ == "__main__":
    print("UC14: Read/Write to a JSON File")
    address_book = AddressBook()

    contact1 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    contact2 = Contact("Jane", "Smith", "456 Oak St", "Chicago", "IL", "60601", "555-5678", "jane.smith@example.com")

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    file_name = "address_book.json"
    address_book.save_to_json(file_name)
    print("\nContents of the JSON file:")
    address_book.load_from_json(file_name)
