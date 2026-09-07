import heapq
queue = []
n = int(input("Enter number of elements: "))
for i in range(n):
    heapq.heappush(queue, int(input("Enter number: ")))
print("Priority Queue:")
while queue:
    print(heapq.heappop(queue), end=" ")