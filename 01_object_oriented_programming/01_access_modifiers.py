# Access Modifiers for Class Attributes.
# Access modifiers determine the visibility or accessibility of class attributes (variables) from outside the class.
# They help enforce encapsulation and control how internal data is exposed or restricted.
# Attributes can be public, private or protected depending on how much access is intended to be allowed.

class User:
    def __init__(self, username: str, email: str, password: str): # UserClass Constructor
        self.username = username # Public attribute
        self._email = email # Protected attribute
        self.__password = password # Private attribute
        
        # Public attributes can be accessed from anywhere, both inside and outside the class.
        # If a class has a public attribute, any other class can call it.

        # Protected attributes are intended to be accessed primarily within the class and by its subclasses.
        # Use a single underscore prefix to indicate protected attributes.

        # Private attributes can only be accessed within the same class where they are defined.
        # These attributes are not accessible from outside class not even from subclasses.
        # Trying to access this outside the classUser returns an AttributeError.
        # Use double underscores prefix to indicate private attributes.

    def get_email(self):
        return self._email 
        
    def get_password(self):
        return self.__password
    
first_user = User("Hope Sain", "hopesain@email.com", "123456")

username = first_user.username # This can be accessed like this since it is a public attribute
print(f"usernameAccess: '{username}'")

bad_email_access = first_user._email # Do not access the email attribute like this....
print(f"badEmailAccess: '{bad_email_access}'")
proper_email_access = first_user.get_email() # Access the protected attribute like this...
print(f"properEmailAccess: '{proper_email_access}'")


proper_password_access = first_user.get_password() # Access the private attributes like this.
print(f"properPasswordAccess: '{proper_password_access}'") 
bad_password_access = first_user.__password # This raises an AttributerError. Strictly private.
        