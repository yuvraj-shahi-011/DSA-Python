n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
maximum = arr[0]
minimum = arr[0]
for i in arr:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print("Maximum:", maximum)
print("Minimum:", minimum)