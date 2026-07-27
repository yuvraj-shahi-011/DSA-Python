rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
matrix = []
print("Enter matrix:")
for i in range(rows):
    matrix.append(list(map(int, input().split())))
for j in range(cols):
    total = 0
    for i in range(rows):
        total += matrix[i][j]
    print("Column", j + 1, "Sum =", total)