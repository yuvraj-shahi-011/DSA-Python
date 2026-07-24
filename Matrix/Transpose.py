rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
matrix = []
print("Enter matrix:")
for i in range(rows):
    matrix.append(list(map(int, input().split())))
print("Transpose:")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()