# Contact Book 


import re  # for email validation 

contacts = []

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern,email)

def is_valid_phone(phone):
    phone = phone.replace(" " ,"").replace("-" ,"")
    return phone.startswith("+") or phone.isdigit()

def add_contact():
    print("\n---Add new Conatct---")
    name = input("Enter Name: ")

    # Phone validation 
    while True:
        phone = input("Enter Phone Number (you may include +country code): ")
        if is_valid_phone(phone):
            break
        else:
            print("Invalid phone format! Try again.")

   # Email validation
    while True:
        email = input("Enter Email(username@domain.com): ")
        if is_valid_email(email):
            break
        else:
            print("Invalid email format! Try again.")


    address = input("Enter Address: ")

    contact = {
        "name" : name ,
        "phone" : phone,
        "email" : email,
        "address" : address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        
    else:
        print("\nContact List: ")
        for i, contact in enumerate(contacts,start=1):
            print(f"{i}.{contact['name']} - {contact['phone']}")

def search_contact():
    search = input("\nEnter name or phone to search: ")

    found = False
    for contact in contacts:
        if search.lower() in contact["name"].lower() or search in contact["phone"]:
            print("\nConatct Found:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            found = True

    if not found:
      print("Contact not found")

def update_contact():
    view_contacts()
    try:
        choice = int (input("\nEnter contact number to update: "))

        if 1 <= choice <=len(contacts):
            contact = contacts[choice - 1]

            print("\nEnter new details(leave blank to keep old value)")

            name = input(f"Name ({contact['name']}:)") or contact['name']

            new_phone = input(f"Phone({contact['phone']}): ") 
            if new_phone:
                if is_valid_phone(new_phone):
                    phone = new_phone
                else:
                    print("Invalid phone! Keeping old number.") 
                    phone = contact['phone']  

            else:
                phone = contact['phone']         


            new_email = input(f"Email({contact['email']}): ") 
            if new_email:
                if is_valid_email(new_email):
                    email = new_email
                else:
                    email = contact['email'] 
            else:
                email = contact['email']           


            address = input(f"Address({contact['address']}): ") or contact['address'] 

            contact.update({
                 "name" : name ,
                 "phone" : phone,
                 "email" : email,
                 "address" : address
            })

            print("Contact updated successfully!")
        else:
            print("Invalid conatct number")

    except:
        print("Invalid input")   


def delete_contact():
    view_contacts()
    try:
        choice = int(input("\nEnter contact number to delete: "))

        if 1 <= choice <= len(contacts):
            removed = contacts.pop(choice-1)
            print(f"contact '{removed['name']}' deleted successfully! ")
        else:
            print("Invalid conatct number!")    


    except:
        print("Invalid Output")           
        

while True:
    print("-------------------")
    print("Contact Book Menu: ")
    print("-------------------")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try: 
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            add_contact()

        elif choice == 2:
            view_contacts()

        elif choice == 3:
            search_contact()

        elif choice == 4:
            update_contact()

        elif choice == 5:
            delete_contact()

        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-6. ")

    except:
        print("Please enter a valid number! ")

        