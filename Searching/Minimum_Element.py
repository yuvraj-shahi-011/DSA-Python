n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
minimum = arr[0]
for i in arr:
    if i < minimum:
        minimum = i
print("Minimum element:", minimum)