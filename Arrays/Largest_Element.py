n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest element is:", largest)
