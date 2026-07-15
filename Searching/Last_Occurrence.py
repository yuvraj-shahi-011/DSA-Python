n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element: "))
for i in range(n - 1, -1, -1):
    if arr[i] == key:
        print("Last occurrence at index", i)
        break
else:
    print("Element not found")