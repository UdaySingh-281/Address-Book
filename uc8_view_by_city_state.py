from collections import defaultdict

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

    def view_by_city_or_state(self):
        city_group = defaultdict(list)
        state_group = defaultdict(list)

        for contact in self.contacts:
            city_group[contact.city].append(contact)
            state_group[contact.state].append(contact)

        return city_group, state_group


if __name__ == "__main__":
    print("UC8: View Contacts Grouped by City or State")
    address_book = AddressBook()

    contact1 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    contact2 = Contact("Jane", "Smith", "456 Oak St", "Chicago", "IL", "60601", "555-5678", "jane.smith@example.com")
    contact3 = Contact("Alice", "Brown", "789 Pine St", "Springfield", "IL", "62701", "555-6789", "alice.brown@example.com")

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    address_book.add_contact(contact3)

    city_group, state_group = address_book.view_by_city_or_state()

    print("Contacts grouped by city:")
    for city, contacts in city_group.items():
        print(f"{city}: {[str(contact) for contact in contacts]}")

    print("\nContacts grouped by state:")
    for state, contacts in state_group.items():
        print(f"{state}: {[str(contact) for contact in contacts]}")
