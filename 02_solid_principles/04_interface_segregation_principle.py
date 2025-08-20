# Interface Segregation Principle (ISP).
"""
It states that do not force any clients to implement an interface which is irrelevant to them.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def eat(self):
        return "Dog is eating."
    
    def sleep(self):
        return "Dog is sleeping."
    
    def speak(self):
        return "Dog is barking."
    
# The above example violates ISP because Dog is forced to implement fly method which is irrelevant to it.
# A better approach would be to create separate interfaces for each animal behavior.
# So make some methods optional if they do not apply to all subclasses.
