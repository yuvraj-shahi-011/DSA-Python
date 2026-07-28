stack = []
n = int(input("Enter number of elements: "))
for i in range(n):
    stack.append(input("Enter element: "))
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Top element:", stack[-1])