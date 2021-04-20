
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
            print(f"searching stack for {item}...")
            if current_head.value == item:
                return True
            current_head = current_head.next
    
        return False

    def remove(self, item):
        current_head = self.head
        
        # checks first node and removes if it's found
        if current_head.value == item:
            self.head = current_head.next
            return current_head

        # checks the rest of the list and removes
        while current_head != None:
            next_node = current_head.next
            if str(next_node) == item:
                node_after_next = next_node.next
                current_head.next = node_after_next
                return next_node

            current_head = current_head.next
    
        return False



    # def pop(self):
    #     if self.is_empty(): return None

    #     popped_node = self.head
    #     self.head = self.head.next
    #     popped_node.next = None
    #     return popped_node.value

    def display(self):
        current_head = self.head
        stack_as_string = ""

        while(current_head != None):
            stack_as_string += f"{current_head.value}\n"
            current_head = current_head.next

        return stack_as_string

    # def peek(self):
    #     if self.is_empty(): return None
    #     return self.head.value


    # def size(self):
    #     stack_size = 0

    #     if self.is_empty():
    #         return stack_size
    #     else:
    #         current_head = self.head
    #         while (current_head != None):
    #             stack_size += 1
    #             current_head = current_head.next
    #         return stack_size

    # def to_list(self):
    #     stack_as_list = []
    #     current_head = self.head
    #     while (current_head != None):
    #         stack_as_list.append(current_head.value)
    #         current_head = current_head.next
        
    #     stack_as_list.reverse()
    #     return stack_as_list 

    def clear(self):
        self.head = None
        return

    # def reverse(self):
    #     current = self.head
    #     temporary = None
    #     previous = None

    #     while (current != None):
    #         temporary = current.next
    #         current.next = previous
    #         previous = current
    #         current = temporary

    #     self.head = previous
    #     return self




