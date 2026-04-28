class User:
    def __init__(self,username,_email,password):
        self.username=username
        self._email=_email
        self.password=password
    def say_hi_to_user(self,user):
        print(f"Sending message to {user.username}: Hi {user.username},its{self.username}")
#Getter and setters
    def get_email(self):
        return self._email
    def set_email(self,newemail):
        self._email=newemail

user1=User("Sandhiya","sd@gmail.com","124")
user2=User("Shrithika","pm@gmail.com","567")
print(user1.get_email())
user1.set_email("bbb@gmail.com")
print(user1.get_email())
print(user1.say_hi_to_user(user2))





        