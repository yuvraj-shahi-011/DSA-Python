rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
matrix = []
print("Enter matrix:")
for i in range(rows):
    matrix.append(list(map(int, input().split())))
key = int(input("Enter element to search: "))
found = False
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == key:
            print("Element found at Row", i + 1, "Column", j + 1)
            found = True
if not found:
    print("Element not found")