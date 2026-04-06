def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        return True
    else:
        return False

users = {"admin": "0000"}
if login(users):
    print("Login successful ")
else:
    print("Invalid username or password ")
    
        