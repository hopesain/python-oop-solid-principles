# Static Methods
# This is a method that belongs to class rather than an instance of a class.
# It turns out that static and class methods have to be covered together.

class Post:
    count_posts = 0 # Class Attribute

    def __init__(self, author: str, content: str):
        self.author = author
        self.content = content
        self.likes = 0
        Post.count_posts += 1

    # Instance method
    def like(self):
        self.likes += 1

    # Class method
    @classmethod
    def total_posts(cls):
        return f"totalPosts: '{cls.count_posts}'"
    
    #Static method.
    @staticmethod
    def greet_reader():
        print("Hello Bruv.")


# Create some posts
p1 = Post("Hope", "Learning Python OOP!")
p2 = Post("Sain", "Writing clean code.")

# Instance method
p1.like()

# Class method
total_posts = Post.total_posts()
print(total_posts)


# Static method
Post.greet_reader()