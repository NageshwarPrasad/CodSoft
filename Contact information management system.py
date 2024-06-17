class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print("\nContact added successfully.\n")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts available.\n")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone']}")
            print("")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            print("")
        else:
            print("\nNo matching contacts found.\n")

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index]['name'] = name
            if phone:
                self.contacts[index]['phone'] = phone
            if email:
                self.contacts[index]['email'] = email
            if address:
                self.contacts[index]['address'] = address
            print("\nContact updated successfully.\n")
        else:
            print("\nInvalid contact index.\n")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            print("\nContact deleted successfully.\n")
        else:
            print("\nInvalid contact index.\n")

def main():
    manager = ContactManager()
    while True:
        print("Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            manager.view_contacts()
            try:
                index = int(input("Enter contact number to update: ")) - 1
                name = input("Enter new name (leave blank to keep current): ")
                phone = input("Enter new phone number (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                address = input("Enter new address (leave blank to keep current): ")
                manager.update_contact(index, name or None, phone or None, email or None, address or None)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.\n")
        elif choice == '5':
            manager.view_contacts()
            try:
                index = int(input("Enter contact number to delete: ")) - 1
                manager.delete_contact(index)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.\n")
        elif choice == '6':
            print("\nExiting Contact Manager. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
