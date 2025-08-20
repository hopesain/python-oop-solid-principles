# Liskov Substitution Principle (LSP)
"""
The Liskov Substitution Principle states that a subclass should be able to be used in place of its superclass, without causing any issues. 
In other words, subclasses should behave in a way that does not break the expectations set by their parent class.

Imagine you wrote a function that accepts a Bird object and expects it to fly and eat.

If you later pass a Penguin (which is technically a bird but cannot fly), your code breaks expectations.

That means Penguin violates LSP, because it cannot fully substitute Bird without surprising behavior.

"""

class Bird:
    def fly(self):
        return "Flying"
    
class Falcon(Bird):
    def fly(self):
        return "Falcon is flying high!"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly!")

def let_bird_fly(bird: Bird):
    print(bird.fly())

let_bird_fly(Falcon())   # ✅ Flying
# let_bird_fly(Penguin())  # ❌ BOOM! Penguins can’t fly

"""
Before I continue with another example.
Let me make something clear about LSP.
Please do not lie about what your class can do. 
If a subclass cannot fully honor the parents' contracts, then restructure your class hierarchy.
"""

# Accepting payments example.

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        raise NotImplementedError("Subclasses must implement this method")
    
class Paychangu(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paying {amount} using Paychangu"

class Malipo(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paying {amount} using Malipo"


def make_payment(method: PaymentMethod, amount: float):
    print(method.pay(amount))

make_payment(Paychangu(), 100)
make_payment(Malipo(), 200)

# The above code works, now imagine we have a free promotion.
class FreeCoupon(PaymentMethod):
    def pay(self, amount: float) -> str:
        raise Exception("Free coupons cannot process payments") # This is a violation of LSP.