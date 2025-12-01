def login_system():
    users = {
        'admin': 'admin123',
        'student': 'student123',
        'parent': 'parent123'
    }

    option = input("LOGIN or SIGNUP: ").upper()

    # SIGNUP
    if option == "SIGNUP":
        new_user = input("Enter new username: ")
        new_pass = input("Enter new password: ")

        if new_user in users:
            return "User already exists."

        users[new_user] = new_pass
        print("Account created! Please log in.\n")
        option = "LOGIN"

    # LOGIN
    if option == "LOGIN":
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            return "Login Successful!"
        else:
            return "Incorrect username or password."

    return "Invalid option."

print(login_system())