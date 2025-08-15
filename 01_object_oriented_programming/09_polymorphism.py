#Polymorphism.
"""
In programming, polymorphism means the same interface can be used for different underlying forms (data types, classes, or functions).
In simple terms, the same operation behaves differently depending on the object it’s acting on.
In python, you can achieve polymorphism through method overriding and duck typing.
In this section, I will only focus on method overriding.
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Snake(Animal):
    def speak(self):
        return "Hiss!"

def animal_sound(animal: Animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
snake = Snake()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(snake) # Output: Hiss!


# What's the actual use case for this???? Are you tired of unnecessary nested if statements?
# This is were polymorphism shines.

"""
Imagine you are building an ecommerce platform that accepts payments via multiple gateways.
Without polymorphism, you might end up with a lot of if-else statements to handle each payment method.
"""

def checkout(gateway_provider: str, amount: float) -> str:
    if gateway_provider == "payChangu":
        # Call payChangu API
        return f"Dear Customer, your payment of {amount} has been processed via payChangu."
    elif gateway_provider == "malipo":
        # Call malipo API
        return f"Dear Customer, your payment of {amount} has been processed via malipo."
    elif gateway_provider == "pawaPay":
        # Call pawaPay API
        return f"Dear Customer, your payment of {amount} has been processed via pawaPay."
    
# This looks nice, but what if you want to add a new payment gateway?
# This code will require you to modify the checkout function, which is not ideal.
# The above code, it's written with a mindset of "If it works, don't touch it."
customer_payment = checkout("payChangu", 100.5)
print(customer_payment)


# Now let's implement this using polymorphism.

class PaymentGateway:
    def pay(self, amount):
        pass

class Paychangu(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"Dear Customer, your payment of {amount} has been processed via payChangu."
    
class Malipo(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"Dear Customer, your payment of {amount} has been processed via malipo."
    
class PawaPay(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"Dear Customer, your payment of {amount} has been processed via pawaPay."
    

def process_payment(gateway: PaymentGateway, amount: float) -> str:
    print("Now using polymorphism to process payment...")
    return gateway.pay(amount)


pay_using_paychangu = process_payment(Paychangu(), 7000)
print(pay_using_paychangu)

pay_using_malipo = process_payment(Malipo(), 5000)
print(pay_using_malipo)

pay_using_pawaPay = process_payment(PawaPay(), 3000)
print(pay_using_pawaPay)

# I hope now you are appreciating the beauty of polymorphism.
# Have you ever heard of the term "interface"?
# In programming, an interface is a contract that defines a set of methods that a class must implement.
# It allows different classes to be treated as the same type as long as they implement the same interface.
# In Python, we can achieve this using abstract base classes (ABCs) from the abc module.

# We implement this using an example of a notification system that sends messages via different channels like email, SMS, and push notifications.

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return f"Sending email notification..."
    
class SMSNotification(Notification):
    def send(self):
        return f"Sending SMS notification..."
    
class PushNotification(Notification):
    def send(self):
        return f"Sending push notification..."
    
# Before  I continue.
# At this point, I believe you are asking yourself, why are abstract base classes important, what happens when you do not include the send method in the inherited class?
# Well, if you do not implement the send method in the inherited class, Python will raise a TypeError when you try to instantiate that class.

class IncompleteNotification(Notification):
    # This class is incomplete and does not implement the send method.
    # Check at the end of this file for its implementation.
    pass


def send_notification(notification: Notification):
    print(notification.send())

email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

send_notification(email)
send_notification(sms)
send_notification(push)


incomplete_notification = IncompleteNotification() # Viola 😂😂