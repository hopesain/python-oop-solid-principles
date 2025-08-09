# Static Attributes
# Attributes that can belong to a class but not to an instance.
# Useful for things like count etc.


class Post:
    count_posts = 0 #Static attribute

    def __init__(self, author: str, content: str):
        self.author = author
        self.content = content
        Post.count_posts += 1

    def display_posts(self):
        return f"Author: '{self.author}', Content: '{self.content}'"
    
first_post = Post("HopeSain", "failedState")
second_post = Post("MirrorCanesat", "hopeLost")

print(Post.count_posts)