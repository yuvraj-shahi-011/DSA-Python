n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
arr.sort()
print("Ascending order:", arr)