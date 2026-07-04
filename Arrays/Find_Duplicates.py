n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
print("Duplicate elements:")
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print(arr[i])