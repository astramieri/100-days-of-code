class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0 # default value

# user_1 = User()
# user_1.user_id = "001"
# user_1.user_name = "angelo"

user_2 = User("001", "angelo")
user_3 = User("002", "serena")

print(f"followers: {user_2.followers}")