import bcrypt
import getpass

passwordFilePath = "passwords.txt"


def register():
    username = input("username $ ")

    if not username.isalnum():
        print("Username must only contain letters and numbers.")
        return

    password1 = getpass.getpass("password $ ")
    password2 = getpass.getpass("password again $ ")

    while password1 != password2:
        print("Passwords do not match.")
        password1 = getpass.getpass("password $ ")
        password2 = getpass.getpass("password again $ ")

    salt = bcrypt.gensalt(12)
    hashed_password = bcrypt.hashpw(password1.encode('utf-8'), salt)

    with open(passwordFilePath, 'a') as file:
        file.write(f"{username}:{hashed_password.decode('utf-8')}:{salt.decode('utf-8')}\n")

    print("Registration successful!")


def login():
    username = input("username $ ")

    try:
        with open(passwordFilePath, 'r') as file:
            for line in file:
                stored_username, stored_password, stored_salt = line.strip().split(':')

                if username == stored_username:
                    break
            else:
                raise ValueError("Username does not exist.")
    except Exception as e:
        print(e)
        return

    password = getpass.getpass("password $ ")

    try:
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print("Login successful!")
        else:
            raise ValueError("Incorrect password.")
    except Exception as e:
        print(e)
        return


while True:
    choice = input("register, login $ ")

    if choice == 'register':
        register()
    elif choice == 'login':
        login()
    elif choice == 'exit':
        print('')
        break
    else:
        print("Invalid option. Please try again.")
