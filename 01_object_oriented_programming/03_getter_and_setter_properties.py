# The pythonic way to attach behaviour to an attribute is to turn an attribute itself into a property.
# Properties are special attributes with additional behaviour.
# Properties can be used in the same way we use regular attributes.
# When you access a property, it's attached getter method is automatically called.
# When you mutate (modify) the property, its setter method gets called.

class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self._email = email
        self.__password = password

    # Add @property decorator for getter property.
    @property
    def email(self):
        return self._email
    
    @property
    def password(self):
        return self.__password
    
    """
    @property
    def password(self):
        raise AttributeError("Password is write only.")
    """

    # Include @attribute.setter for setter property.
    @email.setter
    def email(self, new_email):
        self._email = new_email

    @password.setter
    def password(self, password):
        self.__password = password


new_user = User("Hope Sain", "hopesain@email.com", "123456")

username = new_user.email
print(username)

old_password = new_user.password
print(f"oldPassword: '{old_password}'")
new_user.password = "abcde"
new_password = new_user.password
print(f"newPassword: '{new_password}'")

