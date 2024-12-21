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
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            for contact in self.contacts:
                file.write(str(contact) + '\n')
        print(f"Address book saved to {file_name}")

    def load_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(f"File {file_name} not found.")


if __name__ == "__main__":
    print("UC12: Read/Write to a File Using File I/O")
    address_book = AddressBook()

    contact1 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    contact2 = Contact("Jane", "Smith", "456 Oak St", "Chicago", "IL", "60601", "555-5678", "jane.smith@example.com")

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    file_name = "address_book.txt"
    address_book.save_to_file(file_name)
    print("\nContents of the file:")
    address_book.load_from_file(file_name)
