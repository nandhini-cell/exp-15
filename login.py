def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid credentials"


# Test the function
print(login("admin", "1234"))
print("feature login branch update")