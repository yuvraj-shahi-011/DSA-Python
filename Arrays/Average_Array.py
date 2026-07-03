n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
total = 0
for i in arr:
    total += i
average = total / n
print("Average =", average)