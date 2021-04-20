
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class Stack:
    def __init__(self):
        self.head = None    

    def __str__(self):
        return self.display()

    # def is_empty(self):
    #     if self.head == None: return True
    #     return False
    
    def push(self, item):
        if self.head == None: 
            self.head = Node(item)
            return self
        
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        return self

    def contains(self, item):
        current_head = self.head
        while current_head != None:
            if current_head.value == item:
                return True
            current_head = current_head.next
    
        return False

    def remove(self, item):
        current_head = self.head
        
        if current_head.value == item:
            self.head = current_head.next
            return current_head

        while current_head != None:
            next_node = current_head.next
            if str(next_node) == item:
                node_after_next = next_node.next
                current_head.next = node_after_next
                return next_node

            current_head = current_head.next
    
        return False

    def display(self):
        current_head = self.head
        stack_as_string = ""

        while(current_head != None):
            stack_as_string += f"{current_head.value} "
            current_head = current_head.next

        return stack_as_string

 
    def clear(self):
        self.head = None
        return




