n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element: "))
count = 0
for i in arr:
    if i == key:
        count += 1
print("Occurrences:", count)