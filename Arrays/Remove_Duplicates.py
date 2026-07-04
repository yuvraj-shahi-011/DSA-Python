n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print("Array after removing duplicates:", unique)