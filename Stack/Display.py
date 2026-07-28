stack = []
n = int(input("Enter number of elements: "))
for i in range(n):
    stack.append(input("Enter element: "))
print("Stack Elements:")
for element in reversed(stack):
    print(element)