n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
found = False
for i in arr:
    if i < 0:
        print(i)
        found = True
if not found:
    print("No negative numbers found")