users = {}

def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    users[username] = password
    print("Registration Successful!")

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username] == password:
        print("Login Successful!")
        return True
    else:
        print("Invalid Username or Password")
        return False

def book_trip():
    print("\nAvailable Destinations")
    print("1. Ooty - ₹3000")
    print("2. Kodaikanal - ₹3500")
    print("3. Goa - ₹6000")

    choice = int(input("Choose Destination: "))

    if choice == 1:
        place = "Ooty"
        amount = 3000
    elif choice == 2:
        place = "Kodaikanal"
        amount = 3500
    elif choice == 3:
        place = "Goa"
        amount = 6000
    else:
        print("Invalid Choice")
        return

    print("\nBooking Successful")
    print("Destination:", place)
    print("Amount: ₹", amount)

while True:
    print("\n----- Travel Management System -----")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        if login():
            book_trip()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")