class ProfileManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, age, city, interests):
        self.users[username] = {
            "age": age,
            "city": city,
            "interests": interests
        }

    def get_profile(self, username):
        if username in self.users:
            return self.users[username]
        return "User not found"

    def update_profile(self, username, age=None, city=None, interests=None):
        if username in self.users:
            if age:
                self.users[username]["age"] = age

            if city:
                self.users[username]["city"] = city

            if interests:
                self.users[username]["interests"] = interests

    def show_all_profiles(self):
        for username, profile in self.users.items():
            print(username, ":", profile)