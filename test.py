from hash_table import Hash_Table
TABLE_SIZE = 20


data = ["Ben", "Julie", "Nora", "Emma", "A", "B", "C", "D", "1", "2", "3", "qwerasdfxcv", "1234qwersdfxzcv"]


bens_table = Hash_Table(TABLE_SIZE)
print(bens_table)

for item in data:
    bens_table.insert(item)

print (bens_table)