n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
arr.sort(reverse=True)
print("Descending order:", arr)