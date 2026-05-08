from profiles import ProfileManager
from graph import SocialGraph
from bfs_dfs import bfs_shortest_path, dfs_depth
from recommendation import recommend_friends


pm = ProfileManager()
sg = SocialGraph()


# ADD USERS

pm.add_user("Alice", 20, "Delhi", ["Music", "Gaming", "Coding"])
pm.add_user("Bob", 22, "Mumbai", ["Sports", "Gaming", "Movies"])
pm.add_user("Charlie", 21, "Pune", ["Coding", "Reading", "Music"])
pm.add_user("David", 23, "Chennai", ["Travel", "Music", "Photography"])
pm.add_user("Eva", 20, "Kolkata", ["Gaming", "Movies", "Art"])
pm.add_user("Frank", 24, "Hyderabad", ["Coding", "Sports", "Travel"])
pm.add_user("Grace", 22, "Jaipur", ["Photography", "Music", "Art"])
pm.add_user("Helen", 25, "Bangalore", ["Gaming", "Coding", "Travel"])


# UPDATE PROFILES

pm.update_profile("Alice", city="Gurgaon")
pm.update_profile("Bob", interests=["Sports", "Fitness", "Gaming"])


# SHOW PROFILES

print("\n===== USER PROFILES =====")

print("Alice:", pm.get_profile("Alice"))
print("Bob:", pm.get_profile("Bob"))
print("Charlie:", pm.get_profile("Charlie"))


# ADD CONNECTIONS

sg.add_connection("Alice", "Bob")
sg.add_connection("Alice", "Charlie")
sg.add_connection("Bob", "David")
sg.add_connection("Charlie", "Eva")
sg.add_connection("David", "Frank")
sg.add_connection("Eva", "Grace")
sg.add_connection("Frank", "Helen")
sg.add_connection("Grace", "Helen")
sg.add_connection("Alice", "Eva")
sg.add_connection("Bob", "Frank")


# REMOVE CONNECTION

sg.remove_connection("Alice", "Eva")


sg.display_graph()


# BFS SHORTEST PATH

print("\n===== BFS SHORTEST PATH =====")

path1 = bfs_shortest_path(
    sg.graph,
    "Alice",
    "Helen"
)

print("Path from Alice to Helen:")
print(path1)

path2 = bfs_shortest_path(
    sg.graph,
    "Charlie",
    "Frank"
)

print("Path from Charlie to Frank:")
print(path2)


# DFS EXPLORATION

print("\n===== DFS EXPLORATION =====")

depth2 = dfs_depth(
    sg.graph,
    "Alice",
    2
)

print("Users discovered from Alice with depth 2:")
print(depth2)

depth3 = dfs_depth(
    sg.graph,
    "Alice",
    3
)

print("Users discovered from Alice with depth 3:")
print(depth3)


# FRIEND RECOMMENDATION

print("\n===== FRIEND RECOMMENDATIONS =====")

recommendations = recommend_friends(
    "Alice",
    pm.users
)

for user, score in recommendations:
    print(user, "- Common Interests:", score)