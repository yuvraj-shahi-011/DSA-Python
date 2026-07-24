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
print("Result:")
for i in range(rows):
    for j in range(cols):
        print(A[i][j] + B[i][j], end=" ")
    print()