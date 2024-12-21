from collections import Counter

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


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def count_by_city_or_state(self):
        city_count = Counter(contact.city for contact in self.contacts)
        state_count = Counter(contact.state for contact in self.contacts)
        return city_count, state_count


if __name__ == "__main__":
    print("UC9: Count Contacts by City or State")
    address_book = AddressBook()

    contact1 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    contact2 = Contact("Jane", "Smith", "456 Oak St", "Chicago", "IL", "60601", "555-5678", "jane.smith@example.com")
    contact3 = Contact("Alice", "Brown", "789 Pine St", "Springfield", "IL", "62701", "555-6789", "alice.brown@example.com")

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    address_book.add_contact(contact3)

    city_count, state_count = address_book.count_by_city_or_state()

    print("Number of contacts by city:", city_count)
    print("Number of contacts by state:", state_count)
