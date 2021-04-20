from hash_table import Hash_Map

data = ["Ben", "Julie", "Nora", "Emma", "A", "B", "C", "D", "1", "2", "3"]
TABLE_SIZE = int(len(data) * 1.3)

bens_table = Hash_Map(TABLE_SIZE)
print("\033c")

# bens_table.insert("Ben")
for item in data:
    # print(f"inserting:{item}",end=' ')
    bens_table.insert(item)
print("\n")

print(bens_table)


print("finding Julie at", bens_table.search("Julie"))
print("finding 1 at", bens_table.search("1"))
print("finding Nora at", bens_table.search("Nora"))
print("finding 2 at", bens_table.search("2"))
print("finding Baxter at", bens_table.search("Baxter"))

print("---")

print("removing C:", bens_table.remove("C"))
print("removing C:", bens_table.remove("B"))
print("removing A:", bens_table.remove("A"))
print("removing A:", bens_table.remove("C"))

# print(bens_table)