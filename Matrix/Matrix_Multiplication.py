rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
print("Enter first matrix:")
A = []
for i in range(rows):
    A.append(list(map(int, input().split())))
print("Enter second matrix:")
B = []
for i in range(rows):
    B.append(list(map(int, input().split())))
result = [[0 for j in range(cols)] for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        for k in range(cols):
            result[i][j] += A[i][k] * B[k][j]
print("Result:")
for row in result:
    print(row)