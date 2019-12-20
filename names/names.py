import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
# cache = {} # Cache isn't working properly. Duplicate names not being printed
bst = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

start_time = time.time()

names1 = set(names_1)
duplicates = [names for names in names_2 if names in names1]

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")