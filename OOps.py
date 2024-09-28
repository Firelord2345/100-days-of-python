# class Opp():
#     pass
# opp1=Opp()
# opp1.id="text"
# print(opp1.id)
class User():
    def __init__(self,username,user_id):
        self.name=username
        self.id=user_id
        self.followers=0
        self.following=0
    def follow(self,user):
        self.following+=1
        user.followers+=1
user1=User("Joel",21)
# print(user1.id)
user2=User("Malivia",26)
user2.follow(user1)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)