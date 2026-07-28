stack = []
choice = input("Add element? (yes/no): ")
if choice.lower() == "yes":
    element = input("Enter element: ")
    stack.append(element)
if len(stack) == 0:
    print("Stack is Empty")
else:
    print("Stack is Not Empty")