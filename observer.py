"""
In a real-world web application, the observer dictionary would likely be stored in a database
or a shared data structure to ensure that the list of observers is consistent across all instances of 
the application. Additionally, the chat messages would likely be stored in a database and retrieved 
by the clients as needed. The implementation would also need to handle additional concerns 
such as authentication and authorization, user presence, and error handling.
"""

class ChatRoom:
    def __init__(self):
        self.observers:dict[str,User] = {}

    def register(self, user_id, observer):
        self.observers[user_id] = observer

    def unregister(self, user_id):
        del self.observers[user_id]

    def notify(self, sender, message):
        for user_id, observer in self.observers.items():
            if user_id != sender:
                observer.update(sender, message)

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def update(self, sender, message):
        print(f"{self.user_id} received message from {sender}: {message}")

room = ChatRoom()
user1 = User("User 1")
user2 = User("User 2")
room.register("User 1", user1)
room.register("User 2", user2)
room.notify("User 1", "Hello, User 2!")

