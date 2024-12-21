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

    def search_by_city_or_state(self, city=None, state=None):
        return [contact.__str__() for contact in self.contacts if (city and contact.city == city) or (state and contact.state == state)]


if __name__ == "__main__":
    print("UC7: Search Person by City or State")
    address_book = AddressBook()

    contact1 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "555-1234", "john.doe@example.com")
    contact2 = Contact("Jane", "Smith", "456 Oak St", "Chicago", "IL", "60601", "555-5678", "jane.smith@example.com")

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    city_search = address_book.search_by_city_or_state(city="Springfield")
    print("Contacts in Springfield:", city_search)

    state_search = address_book.search_by_city_or_state(state="IL")
    print("Contacts in IL:", state_search)
