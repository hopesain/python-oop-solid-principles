# Getter and Setter Methods
# These methods are used to control access to and modification of class attributes particularly protected and private attributes.
# Getter (Accessors) methods are used to retrieve the value of an attribute.
# Setter (Mutators) methods are used to modify or set new value for an attribute.

class User:
    def __init__(self, username: str, email: str, password: str): #userClassConstructor.
        self.username = username #publicAttribute
        self._email = email #protectedAttribute
        self.__password = password #privateAttribute

    #getterMethodsBelow
    #A getter method, isn't something new. You prolly saw it in the previous topic on access modifiers.
    def get_username(self):
        return f"userName: {self.username}"
    
    def get_email(self):
        return f"userEmail: {self._email}" 
    
    def get_password(self):
        return f"userPassword: {self.__password}"
    
    #setterMethodsBelow
    def set_username(self, new_username):
        self.username = new_username

    def set_email(self, new_email):
        self._email = new_email

    def set_password(self, new_password):
        self.__password = new_password

    # Let's add some logic to setters for email and password.
    # Password should not have less than six characters.
    # Let's name this new methon, "set_new_password"
    def set_new_password(self, new_password):
        if isinstance(new_password, str) and len(new_password) > 6: #len counts the number characters.
            self.__password = new_password
        else:
            print("Password must have not less than six characters.")


sample_user = User("Hope Sain", "hopesain@email.com", "123456")

#Using the Getter Method.
username = sample_user.get_username()
print(username)
email = sample_user.get_email()
print(email)
password = sample_user.get_password()
print(password)

#Using the Setter Method.
#Use the same approach for other attributes.
sample_user.set_email("hopesainofficial@email.com")
email = sample_user.get_email()
print(email)
    
#Setting new user with a password less than six characters.
#First checking old password then trying to modify it wrongly.
#Wrongly is subjective to our example role, lol... 
old_password = sample_user.get_password()
print(f"Old Password: {old_password}")
sample_user.set_new_password(789)
new_password = sample_user.get_password() #Wrongly, lol.
print(new_password)
sample_user.set_new_password("1234abcd") #Rightly, lol.
new_password = sample_user.get_password()
print(f"newPassword: '{new_password}'") #Viola...