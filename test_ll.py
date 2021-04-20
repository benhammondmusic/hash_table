from linked_list_stack import Stack

bens_stack = Stack()
bens_stack.push("a")
bens_stack.push("b")
bens_stack.push("c")
print(bens_stack)

# print(bens_stack.contains("4"))
# print(bens_stack.contains("a"))
bens_stack.remove("c")
print("---")
print(bens_stack)
bens_stack.remove("a")
print("---")
print(bens_stack)
bens_stack.remove("b")
print("---")
print(bens_stack)
