class User:
    def __init__(self):
        self.users = {}

    def sign_up(self, username, password):
        if username in self.users:
            print("Username already exists. Please try again.")
            return False
        self.users[username] = password
        print("User signed up successfully.")
        return True

    def sign_in(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Signed in successfully.")
            return True
        print("Invalid username or password. Please try again.")
        return False
