from linked_list_stack import Stack

class Hash_Map():
    def __init__(self, TABLE_SIZE):
        self.table = []

        for idx in range(TABLE_SIZE):
            self.table.append(Stack())

    def __str__(self):
        table_display = ""
        for idx in range(len(self.table)):
            table_display += f"{str(idx)}: {str(self.table[idx])}\n"
        return table_display
    
    def get_hash(self, item):
        hash_index = 0
        for char in item:
            hash_index += ord(char)
        return hash_index % len(self.table)

    def insert(self, item):
        hashed_index = self.get_hash(item)
        stack = self.table[hashed_index]
        stack.push(item)


    def search(self, item):
        hashed_index = self.get_hash(item)
        stack = self.table[hashed_index] 
        if stack.contains(item):
            return hashed_index
        return -1

    def remove(self, item):
        hashed_index = self.get_hash(item)
        stack = self.table[hashed_index] 
        if stack.remove(item): return item
        return False
