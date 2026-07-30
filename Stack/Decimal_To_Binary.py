stack = []
number = int(input("Enter decimal number: "))
while number > 0:
    stack.append(number % 2)
    number = number // 2
print("Binary Number:")
while stack:
    print(stack.pop(), end="")