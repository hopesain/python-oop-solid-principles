# Open-Closed Principle (OCP)
"""
Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
"""

# Remember that AuthService in SRP?
# It does not follow OCP. Let me bring it back here.

class BadAuthService:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def login(self):
        print(f"Welcome back, '{self.username}'! You have successfully logged in with the email '{self.email}'.")

    def logout(self):
        print(f"Thank you for visiting our platform, '{self.username}'! You have successfully logged out.")

# The above code looks fine and clean right?
# Wait until we want to login with Google, Facebook, X, Github. I believe you can see surgery of our existing codebase. lol.
# Now let us refactor it....

from abc import ABC, abstractmethod

class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

class LoginMethod(ABC):
    @abstractmethod
    def login(self, user: User):
        pass
    
class GmailLogin(LoginMethod):
    def login(self, user: User):
        print(f"'{user.username}' logged in using Gmail account.")

class FacebookLogin(LoginMethod):
    def login(self, user: User):
        print(f"'{user.username}' logged in using Facebook account.")

class GithubLogin(LoginMethod):
    def login(self, user: User):
        print(f"'{user.username}' logged in using Github account.")

class AuthService:
    def __init__(self, login_method: LoginMethod):
        self.login_method = login_method

    def login(self, user: User):
        self.login_method.login(user)


# clientCode.

first_user = User("hopesain", "hopesain@email.com", "password123")

gmail_login = GmailLogin()
facebook_login = FacebookLogin()
github_login = GithubLogin()

login_via_gmail = AuthService(gmail_login)
login_via_gmail.login(first_user)

login_via_facebook = AuthService(facebook_login)
login_via_facebook.login(first_user)

login_via_github = AuthService(github_login)
login_via_github.login(first_user)

# anotherExample.
# will share it later, lol.
