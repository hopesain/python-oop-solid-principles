# Inheritance
"""
Inheritance  allows a new class (child class or derived class) to inherit attributes and methods from an existing class (parent class or base class). 
This mechanism promotes code reusability and establishes an "is-a" relationship between classes
"""

# Simple Syntax.
class ParentClass:
    def __init__(self, parent_attribute: str):
        self.parent_attribute = parent_attribute

    def parent_method(self):
        print(f"Method from the ParentClass with '{self.parent_attribute}'")

class ChildClass(ParentClass): #ChildClass inherits from ParentClass
    def __init__(self, parent_attribute, child_attribute: str):
        super().__init__(parent_attribute) # Call ParentClass Constructor.
        self.child_attribute = child_attribute

    def child_method(self):
        print(f"Method from ChildClass with '{self.child_attribute}' inherited from '{self.parent_attribute}' ")


# Should we use this simple implementation or you are confused???
# You wanna hear my assumption, you are confused, 😂.

# Starting over.
"""
From my understanding, the whole point of inheritance is that you do not have to repeat yourself on related items and attributes.

Let's say you are working on a School Management System. You have an object, User (firstname, lastname, username, phonenumber, email and password), then you have other objects Student, Lecturer, Librarian and others which can inherit from the parentClass User.

Still doesn't ring a bell??

Let's also say that you have two objects, namely a Car and Motobyke. They both have a brand, model and year. In simple terms, they are both Vehicles. 
They both have a default behaviour (method), they start and stop.

Want another example, let me think about it first. But for the meantime, let's make the above examples into code. 
"""
