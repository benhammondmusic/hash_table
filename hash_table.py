TABLE_SIZE = 20
data = ["Ben", "Julie", "Nora", "Emma", "A", "B", "C", "D", "1", "2", "3", "qwerasdfxcv", "1234qwersdfxzcv"]


def hash(value):
    hash_index = 0
    for char in value:
        hash_index += ord(char)
    return hash_index % TABLE_SIZE

hash_table = [None] * TABLE_SIZE


for item in data:
    hashed_index = hash(item)
    print(f"ITEM: {item} INDEX: {hashed_index}")
    if hash_table[hashed_index] == None:
        hash_table[hashed_index] = item
    else:
        # chain with string concat if there are collisions
        hash_table[hashed_index] = hash_table[hashed_index] + " " + item


print("HASH TABLE", hash_table)