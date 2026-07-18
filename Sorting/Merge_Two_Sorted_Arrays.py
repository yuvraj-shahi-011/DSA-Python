n1 = int(input("Enter size of first array: "))
arr1 = list(map(int, input("Enter first sorted array: ").split()))
n2 = int(input("Enter size of second array: "))
arr2 = list(map(int, input("Enter second sorted array: ").split()))
merged = arr1 + arr2
merged.sort()
print("Merged sorted array:", merged)