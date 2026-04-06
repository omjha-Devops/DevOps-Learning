users = {
    "admin": "1234",
    "omjha": "5678"
}
username = input("Enter your username: ")
password = input("Enter your password: ")
if username in users and users[username] == password:
    print("Login successful ")
else:
    print("Invalid username or password ")