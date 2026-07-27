rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
matrix = []
print("Enter matrix:")
for i in range(rows):
    matrix.append(list(map(int, input().split())))
for i in range(rows):
    print("Row", i + 1, "Sum =", sum(matrix[i]))