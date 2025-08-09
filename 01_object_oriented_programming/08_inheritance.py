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

# SCHOOL MANAGEMENT SYSTEM EXAMPLE

class User:
    def __init__(self, firstname: str, lastname: str, username: str, email: str):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email 

    def greet_user(self):
        print(f"Hello {self.firstname.capitalize()} {self.lastname.capitalize()}")

class Student(User):
    def __init__(self, firstname: str, lastname: str, username: str, email: str, program: str, year_of_study: int):
        super().__init__(firstname, lastname, username, email)
        self.program = program
        self.year_of_study = year_of_study

    def display_student_information(self):
        self.greet_user() #Inherited method
        print(f"Program: {self.program}")
        print(f"Year of Study: {self.year_of_study}")

class Lecturer(User):
    def __init__(self, firstname: str, lastname: str, username: str, email: str, department: str):
        super().__init__(firstname, lastname, username, email)
        self.department = department

    def display_lecturer_information(self):
        self.greet_user() #Inherited method
        print(f"You are a lecturer in {self.department}")


first_student = Student("John", "Doe", "johndoe", "johndoe@email.com", "Computer Science", 2)
first_student.display_student_information()
first_student.greet_user() #Inherited method

first_lecturer = Lecturer("Jane", "Smith", "janesmith", "janesmith@email.com", "Mathematics")
first_lecturer.display_lecturer_information()

# VEHICLE EXAMPLE