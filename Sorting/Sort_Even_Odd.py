n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
even = []
odd = []
for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
even.sort()
odd.sort()
print("Even numbers:", even)
print("Odd numbers:", odd)