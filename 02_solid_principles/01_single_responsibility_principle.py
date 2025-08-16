# S on SOLID acronym stands for Single Responsibility Principle (SRP).
# This principle states that a class should have only one reason to change, meaning that a class should only have one job or responsibility.
# In other words, a class should only do one thing and do it well.

# The best way to explain this is through an example.

class BadUserClass:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_user(self):
        return {"name": self.name, "email": self.email}

    def delete_user(self):
        # Code to delete user
        pass

    def update_user(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def send_email(self, message: str):
        print(f"Sending email to {self.email}: {message}")

    def login(self):
        print(f"{self.name} logged in.")

    def logout(self):
        print(f"{self.name} logged out.")

# This class has multiple responsibilities: managing user data, sending emails, and handling login/logout functionality.

# Now, let's refactor this class to adhere to the Single Responsibility Principle:
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def get_user(self):
        return {"username": self.username, "email": self.email}
    
    def update_user(self, new_username: str, new_email: str):
        self.username = new_username
        self.email = new_email
        return f"Updated user: {self.username}, {self.email}"
    

class EmailService:
    def send_welcome_email(self, user: User):
        print(f"Sending welcome email to {user.email} for user {user.username}")



class AuthService:
    def login(self, user: User):
        print(f"{user.username} logged in.")

    def logout(self, user: User):
        print(f"{user.username} logged out.")


# clientCode
user = User("hopesain", "hopesain@email.com")
print(user.get_user())
user.update_user("hope_sain", "HopeSainOfficial@email.com")
print(user.get_user())

email = EmailService()
email.send_welcome_email(user)

authentication = AuthService()
authentication.login(user)
authentication.logout(user)