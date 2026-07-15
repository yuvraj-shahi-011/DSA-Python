n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
maximum = arr[0]
for i in arr:
    if i > maximum:
        maximum = i
print("Maximum element:", maximum)