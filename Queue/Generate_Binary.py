from collections import deque
n = int(input("Enter value of n: "))
queue = deque()
queue.append("1")
for i in range(n):
    front = queue.popleft()
    print(front)
    queue.append(front + "0")
    queue.append(front + "1")