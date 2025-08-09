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

# As much as the code now looks much cleaner when using @property, the pythonic way. But I just have an opinion that I would not implement them in a production level code.
# My opinion is solely based on the docs I  have read and interact with our good friend, chatGPT 😂.
# As you are practicing, kindly read this. https://realpython.com/python-getter-setter/#using-properties-instead-of-getters-and-setters-the-python-way

# When to use Getter and Setter Properties.
# 1. To enforce validation when assigning values.
# 2. When you want attributes to be read-only or write-only

# When not to use Getter and Setter Properties.
# 1. When the operation is CPU or I/O bound.
# 2. When debugging is needed, properties can hide behavior.
# 3. When working with inheritance or overriding.
# 4. When building a public API.

# In summary, To crown it all, In a nutshell, Never use them. That's my take.