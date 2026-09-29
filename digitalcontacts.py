contacts = []
file_name = "contacts.txt"


def load_contacts():
    try:
        file = open(file_name, "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) == 3:
                contact = {
                    "name": data[0],
                    "phone": data[1],
                    "email": data[2]
                }
                contacts.append(contact)

        file.close()

    except FileNotFoundError:
        pass


def save_contacts():
    file = open(file_name, "w")

    for contact in contacts:
        file.write(
            contact["name"] + "|" +
            contact["phone"] + "|" +
            contact["email"] + "\n"
        )

    file.close()


def add_contact():
    print("\n--- Add Contact ---")

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if name == "" or phone == "":
        print("Name and phone number are required.")
        return

    for contact in contacts:
        if contact["phone"] == phone:
            print("This phone number already exists.")
            return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts()
    print("Contact added successfully!")


def view_contacts():
    print("\n--- All Contacts ---")

    if len(contacts) == 0:
        print("No contacts available.")
        return

    for i in range(len(contacts)):
        print("\nContact", i + 1)
        print("Name:", contacts[i]["name"])
        print("Phone:", contacts[i]["phone"])
        print("Email:", contacts[i]["email"])


def search_contact():
    print("\n--- Search Contact ---")

    search_name = input("Enter name to search: ").strip().lower()
    found = False

    for contact in contacts:
        if search_name in contact["name"].lower():
            print("\nContact Found")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if found == False:
        print("Contact not found.")


def update_contact():
    print("\n--- Update Contact ---")

    phone = input("Enter phone number of contact to update: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            print("Leave a field blank to keep its current value.")

            new_name = input("Enter new name: ").strip()
            new_phone = input("Enter new phone number: ").strip()
            new_email = input("Enter new email: ").strip()

            if new_name != "":
                contact["name"] = new_name

            if new_phone != "":
                contact["phone"] = new_phone

            if new_email != "":
                contact["email"] = new_email

            save_contacts()
            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")

    phone = input("Enter phone number of contact to delete: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts()
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def main():
    load_contacts()

    while True:
        print("\n===== DIGITAL CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Thank you for using Digital Contact Book!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


main()
