class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0  # default value
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


# user_1 = User()
# user_1.user_id = "001"
# user_1.user_name = "angelo"

user_2 = User("001", "angelo")
user_3 = User("002", "serena")

user_2.follow(user_3)

print(f"user_2.followers: {user_2.followers}")
print(f"user_2.following: {user_2.following}")

print(f"user_3.followers: {user_3.followers}")
print(f"user_3.following: {user_3.following}")

