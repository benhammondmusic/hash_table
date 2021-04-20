""" Methods for any Hash Table must include:
x - search()
x - insert()
- remove() """

class Hash_Table():
    def __init__(self, TABLE_SIZE):
        self.table = [""] * TABLE_SIZE

    def __str__(self):
        return '|'.join([str(elem) for elem in self.table])
    
    def get_hash(self, item):
        hash_index = 0
        for char in item:
            hash_index += ord(char)
        return hash_index % 20

    def insert(self, item):
        hashed_index = self.get_hash(item)
        # print(f"ITEM: {item} INDEX: {hashed_index}")
        if self.table[hashed_index] == "":
            self.table[hashed_index] = item
        else:
            # chain with string concat if there are collisions
            self.table[hashed_index] = self.table[hashed_index] + " " + item

    def search(self, item):
        hashed_index = self.get_hash(item)
        # print(f"ITEM: {item} INDEX?: {hashed_index}")
        if self.table[hashed_index] and item in self.table[hashed_index]: 
            return hashed_index
        return -1

    def remove(self, item):
        item_index = self.search(item)
        if item_index < 0:
            print(f"Error, item {item} not found in list and could not be removed")
            return False

        removed_item = self.table[item_index]
        self.table[item_index] = ""
        print(f"Item: {removed_item} has been removed")
        # ! FIX THIS TO ACCOUNT FOR CHAINED / LINKED LIST 
        return removed_item