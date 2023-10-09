class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        if len(self.id) < 3:
            print("UserId not Valid")
            return
        if username == "":
            print("Username ERROR.")
            return
        print("User created successfully.")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Xia")
user2 = User("002", "DARK")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)


