rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
matrix = []
print("Enter matrix:")
for i in range(rows):
    matrix.append(list(map(int, input().split())))
largest = matrix[0][0]
for row in matrix:
    for num in row:
        if num > largest:
            largest = num
print("Largest element =", largest)