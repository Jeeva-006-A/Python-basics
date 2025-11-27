#Write your code here
class User:
    def __init__(self):
        self.current_user = {}
    def add_user(self, username,password):
        self.current_user = {"username":username, "password":password, "login_status": False, 'active':True}
    
user1 = User()
user1.add_user("john", "1234")
print(user1.current_user)