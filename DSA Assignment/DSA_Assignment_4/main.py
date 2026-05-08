from bst import BST
from graph import Graph
from hash_table import HashTable


print("===== BINARY SEARCH TREE =====")

bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

print("Inorder Traversal:")
bst.inorder(bst.root)

print("\n")

result = bst.search(bst.root, 40)

if result:
    print("40 Found in BST")
else:
    print("40 Not Found")


print("\n===== GRAPH BFS AND DFS =====")

g = Graph()

g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(2, 4, 4)

g.bfs(0)
g.dfs(0)


print("\n===== HASH TABLE =====")

ht = HashTable(5)

ht.insert(1, "Apple")
ht.insert(6, "Banana")
ht.insert(11, "Mango")

ht.display()

print("Search Key 6:", ht.search(6))

ht.delete(6)

print("After Deletion:")

ht.display()