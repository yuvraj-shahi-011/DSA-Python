n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element: "))
for i in range(n):
    if arr[i] == key:
        print("First occurrence at index", i)
        break
else:
    print("Element not found")