def load_contacts(filename):

    contacts = {}

    try:

        with open(filename, "r") as f:

            for line in f:

                name, phone = line.strip().split(",")

                contacts[name] = phone

    except FileNotFoundError:

        pass

    return contacts





def save_contacts(filename, contacts):

    with open(filename, "w") as f:

        for name, phone in contacts.items():

            f.write(f"{name},{phone}\n")





def add_contact(contacts):

    name = input("Enter contact name: ").strip()

    phone = input("Enter phone number: ").strip()

    contacts[name] = phone

    print("Contact added.")





def view_contacts(contacts):

    if not contacts:

        print("No contacts found.")

    else:

        for name, phone in contacts.items():

            print(f"{name}: {phone}")





def search_contact(contacts):

    name = input("Enter name to search: ").strip()

    if name in contacts:

        print(f"{name}: {contacts[name]}")

    else:

        print("Contact not found.")





def main():

    FILENAME = "contacts.txt"

    contacts = load_contacts(FILENAME)



    while True:

        print("\nMenu:\n1. Add\n2. View\n3. Search\n4. Quit")

        choice = input("Choose an option (1-4): ")



        if choice == "1":

            add_contact(contacts)

        elif choice == "2":

            view_contacts(contacts)

        elif choice == "3":

            search_contact(contacts)

        elif choice == "4":

            save_contacts(FILENAME, contacts)

            print("Contacts saved!")

            break

        else:

            print("Invalid input. Try again.")





if __name__ == "__main__":

    main()

