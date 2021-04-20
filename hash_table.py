""" Methods for any Hash Table must include:
- search()
x - insert()
- remove() """

class Hash_Table():
    def __init__(self, TABLE_SIZE):
        self.table = [None] * TABLE_SIZE

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
        if self.table[hashed_index] == None:
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