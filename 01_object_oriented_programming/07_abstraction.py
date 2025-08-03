# Abstraction.
# The process of hiding complex implementation of details and showing only the essential features of an object or concept.
# The user of the class does not need to know how it does.
# Encapsulation "Do not touch the engine, use the keys"
# Abstraction "You do not need to know how the engine works, just drive."

#First Example.
"""
Imagine we have an EmailService class, for a user to send an email the following steps takes place in the backgound.
You first connect the user to the server.
Authenticate User.
Send the email.
Disconnect from the server.

But we only expose the send_email method and the class user does not need to know what happens in the background.
"""

class EmailService:
    def __init__(self, sender: str, recipient: str, message: str):
        self.sender = sender
        self.recipient = recipient
        self.message = message

    def send_email(self):
        self.__connect_to_server()
        self.__authenticate_user()
        self.__send_message()
        self.__disconnect()
        

    def __connect_to_server(self):
        print("Connecting to the server......")
    
    def __authenticate_user(self):
        print("Print authenticating the user.......")

    def __send_message(self):
        print(f"From: '{self.sender}' // To: '{self.recipient}', Message: '{self.message}'")

    def __disconnect(self):
        print("Disconnecting from the server...")
    

first_email = EmailService("hope@email.com", "sain@email.com", "What color is your bughatti.")
first_email.send_email()

# Second Example.
"""
Let's take VLC or any other media players.
You hit that Play icon or button.
Can you guess what happens in the background?
It loads the video from the file path.
Decodes the video and finally renders it.
All you had to know was how to hit the play button and know nothing about what happens in the background.
"""

class VideoPlayer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        
    def play(self):
        self.__load_file()
        self.__decode_video()
        self.__render()

    def __load_file(self):
        print(f"Loading video from '{self.file_path}'")

    def __decode_video(self):
        print("Decoding the video...")

    def __render(self):
        print("Rendering video....")


favorite_show = VideoPlayer("Downloads/")
favorite_show.play()