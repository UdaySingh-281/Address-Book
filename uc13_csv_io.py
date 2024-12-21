import csv

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

    def save_to_csv(self, file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.contacts[0].to_dict().keys())
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())
        print(f"Address book saved to {file_name}")

    def load_from_csv(self, file_name):
        try:
            with open(file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print(f"File {file_name} not found.")


if __name__ == "__main__":
    print("UC13: Read/Write to a CSV File")
    address_book = AddressBook()

    contact1 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    contact2 = Contact("Jane", "Smith", "456 Oak St", "Chicago", "IL", "60601", "555-5678", "jane.smith@example.com")

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    file_name = "address_book.csv"
    address_book.save_to_csv(file_name)
    print("\nContents of the CSV file:")
    address_book.load_from_csv(file_name)
