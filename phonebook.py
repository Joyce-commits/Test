# phone book project name, phone number, email id, dob, category
import sys

# function to get the nummber of rows from the user
def initial_phonebook():
    rows = int(input("Please enter initial number of contacts: "))
    cols = 5

    # Array to store phonebook details
    phone_book = []

    # User input for contact details
    # 0 - name, 1 - number, 2 - email, 3 - dob, 4 - category
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY): " % (i + 1))

        temp = []
        for j in range(cols):
                if j == 0:
                    temp.append(str(input("Enter name*: ")))
                    if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Name is a mandatory field. Process exiting due to blank field...")
                if j == 1:
                    temp.append(int(input("Enter number*: ")))
                    if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Number is a mandatory field. Process exiting due to blank field...")
                if j == 2:
                    temp.append(str(input("Enter e-mail address: ")))
                    if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
                if j == 3:
                    temp.append(str(input("Enter date of birth (dd/mm/yy): ")))
                    if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
                if j == 4:
                    temp.append(str(input("Enter category: ")))
                    if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
        
        phone_book.append(temp)


        print(phone_book)
        return phone_book

def menu():
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def add_contact(phone_book):
    name = input("Enter name: ")
    number = int(input("Enter number: "))
    email = input("Enter email address: ")
    dob = input("Enter date of birth (dd/mm/yy): ")
    category = input("Enter category: ")
    contact = [name, number, email, dob, category]
    phone_book.append(contact)
    print("Contact added successfully!")
    return phone_book


def search_contact(phone_book):
    name = input("Enter name to search: ")
    found = False
    for contact in phone_book:
        if contact[0] == name:
            print("Contact found!")
            print("Name: ", contact[0])
            print("Number: ", contact[1])
            print("Email: ", contact[2])
            print("Date of Birth: ", contact[3])
            print("Category: ", contact[4])
            found = True
            break
    if not found:
        print("Contact not found!")
    return phone_book

def update_contact(phone_book):
    name = input("Enter name to update: ")
    found = False
    for contact in phone_book:
        if contact[0] == name:
            print("Contact found!")
            print("1. Update number")
            print("2. Update email")
            print("3. Update date of birth")
            print("4. Update category")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                contact[1] = int(input("Enter new number: "))
            elif choice == 2:
                contact[2] = input("Enter new email address: ")
            elif choice == 3:
                contact[3] = input("Enter new date of birth (dd/mm/yy): ")
            elif choice == 4:
                contact[4] = input("Enter new category: ")
            else:
                print("Invalid choice!")
            print("Contact updated successfully!")
            found = True
            break
    if not found:
        print("Contact not found!")
    return phone_book

def remove_contact(phone_book):
    name = input("Enter name to remove: ")
    found = False
    for contact in phone_book:
        if contact[0] == name:
            phone_book.remove(contact)
            print("Contact removed successfully!")
            found = True
            break
    if not found:
        print("Contact not found!")
    return phone_book



def thanks():
    print("Thank you for using the phone book program!")
    sys.exit()
    return phone_book


def main():
    phone_book = initial_phonebook()
    while True:
        choice = menu()
        if choice == 1:
            phone_book = add_contact(phone_book)
        elif choice == 2:
            phone_book = search_contact(phone_book)
        elif choice == 3:
            phone_book = update_contact(phone_book)
        elif choice == 4:
            phone_book = remove_contact(phone_book)
        elif choice == 5:
            thanks()
        else:
            print("Invalid choice! Please try again.")
        print(phone_book)

main()

   

        
        