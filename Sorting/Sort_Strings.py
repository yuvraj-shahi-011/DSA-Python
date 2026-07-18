n = int(input("Enter number of words: "))
words = []
for i in range(n):
    words.append(input())
words.sort()
print("Sorted words:")
for word in words:
    print(word)