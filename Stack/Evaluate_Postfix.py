stack = []
expression = input("Enter postfix expression (single-digit numbers): ")
for ch in expression:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == "+":
            stack.append(a + b)
        elif ch == "-":
            stack.append(a - b)
        elif ch == "*":
            stack.append(a * b)
        elif ch == "/":
            stack.append(a // b)
print("Answer:", stack.pop())