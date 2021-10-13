from collections import Counter

words = []

for _ in range(int(input())):
    words.append(input())

print(len(Counter(words)))

print(*Counter(words).values())