# Encapsulation in Python.
# Encapsulation is basically about hiding the internal staff and only exposing what is necessary, through a controlled interface.
# Encapsulation is a principle in software design where internal details are hidden and only necessary parts are exposed to use.
# Let's try this example, "Don't touch the engine to start the car, just use the keys."
"""
You do not start a car by poking wires in the engine.
You use a key or a start button, that's an interface.
The engine is complex, powerful, yet hidden.
The key gives you controlled access to that power.
You cannot and should not mess with the engine directly. You might break it or misuse it.
This my dear friend is what we call ENCAPSULATION. 
"""
# CAR EXAMPLE.

class Car:
    def __init__(self, car_brand: str):
        self.car_brand = car_brand
        self.__engine_status = "off"   #Private attribute.

    #Interface (start and stop methods.)
    def start(self):
        self.__engine_status = "on"
        # You might add more logic here to get the car started. Unfortunately, I'm not a core car person, lol.
        print(f"Your {self.car_brand} has started, please enjoy your ride...")

    def stop(self):
        self.__engine_status = "off"
        print(f"Your {self.car_brand} has stopped, hope you enjoyed the ride...")

first_car = Car("Feralli")
first_car.start()
first_car.stop()

# Still does not ring a bell, let us try a BankAccount example.

class BankAccount:
    def __init__(self, account_name: str):
        self.account_name = account_name
        self.__balance = 0.00 #Hidden attribute, cannot be accessed directly.

    def get_balance(self):
        print(f"Dear {self.account_name} your current balance is MK{self.__balance}")
    
    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Invalid deposit amount: 'Amount must be positive.'")
        self.__balance += amount
        print(f"Dear {self.account_name}, your account has been credited MK{amount} and your new balance is MK{self.__balance}")
    
    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Invalid withdraw amount: 'Amount must be positive.'")
        elif amount >= self.__balance:
            raise ValueError("Insufficient funds...")
        self.__balance -= amount
        print(f"Dear {self.account_name}, your account has been debited MK{amount}, your new balance is MK{self.__balance}")



first_account = BankAccount("HopeSain")
first_account.get_balance()
first_account.deposit(10000)
first_account.withdraw(4000)
first_account.get_balance()
first_account.withdraw(15000) # This raises a ValueError.