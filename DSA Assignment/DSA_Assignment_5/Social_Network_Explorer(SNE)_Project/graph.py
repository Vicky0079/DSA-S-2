class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_connection(self, user1, user2):
        if user1 not in self.graph:
            self.graph[user1] = []

        if user2 not in self.graph:
            self.graph[user2] = []

        self.graph[user1].append(user2)
        self.graph[user2].append(user1)

    def remove_connection(self, user1, user2):
        if user2 in self.graph[user1]:
            self.graph[user1].remove(user2)

        if user1 in self.graph[user2]:
            self.graph[user2].remove(user1)

    def get_friends(self, user):
        return self.graph.get(user, [])

    def display_graph(self):
        print("\nSocial Network Connections:")

        for user, friends in self.graph.items():
            print(user, "->", friends)