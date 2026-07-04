n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
arr.sort()
print("Second largest =", arr[-2])