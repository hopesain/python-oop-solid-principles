# Dependency Inversion Principle (DIP).
"""
It states that high-level modules should not depend on low-level modules. Both should depend on abstractions.
Additionally, abstractions should not depend on details. Details should depend on abstractions.
"""

# Bad Implementation Example.
class SQLiteDatabase:
    def save(self, data: str):
        return f"Saving '{data}' to SQLite database"


class BadUserService:
    def __init__(self):
        self.db = SQLiteDatabase()   # directly tied to SQLite

    def create_user(self, name: str):
        self.db.save(name)

"""
Here, BadUserService (a high-level class) depends directly on SQLiteDatabase (a low-level detail).
If you switch to PostgreSQL, MySQL, MongoDB, or even a file system, you’re screwed.
"""

# Good Implementation Example.

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data: str):
        pass

class MySQLDatabase(Database):
    def save(self, data: str):
        return f"Saving '{data}' to MySQL database"

class PostgreSQLDatabase(Database):
    def save(self, data: str):
        return f"Saving '{data}' to PostgreSQL database"

class MongoDBDatabase(Database):
    def save(self, data: str):
        return f"Saving '{data}' to MongoDB database"
    
class UserService:
    def __init__(self, database: Database):
        self.database = database # Depends on abstraction, not on a specific database implementation

    def create_user(self, name: str):
        self.database.save(name)


# Another example. Notification System.
class Notifier(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class EmailNotifier(Notifier):
    def send_notification(self, message: str):
        return f"Sending email notification with message: {message}"
    
class SMSNotifier(Notifier):
    def send_notification(self, message: str):
        return f"Sending SMS notification with message: {message}"
    
class PushNotifier(Notifier):
    def send_notification(self, message: str):
        return f"Sending push notification with message: {message}"
    
class BookAppointment:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def book_appointment(self, user: str):
        message = f"Booking appointment for {user}"
        return self.notifier.send_notification(message)
    
# clientCode
email_notifier = EmailNotifier()
push_notifier = PushNotifier()

first_appointment = BookAppointment(email_notifier)

print(first_appointment.book_appointment("Hope Sain"))