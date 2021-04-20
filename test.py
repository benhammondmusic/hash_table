from hash_table import Hash_Table
TABLE_SIZE = 20


data = ["Ben", "Julie", "Nora", "Emma", "A", "B", "C", "D", "1", "2", "3", "qwerasdfxcv", "1234qwersdfxzcv"]


bens_table = Hash_Table(TABLE_SIZE)
print(bens_table)

for item in data:
    print(f"inserting:{item}")
    bens_table.insert(item)

print(bens_table)
print("---")
print("finding Julie at", bens_table.search("Julie"))
print("finding 1 at", bens_table.search("1"))
print("finding Nora at", bens_table.search("Nora"))
print("finding Baxter at", bens_table.search("Baxter"))

