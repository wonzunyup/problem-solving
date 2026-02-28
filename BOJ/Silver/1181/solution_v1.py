import sys

input = sys.stdin.readline

N = int(input())

words = []
for _ in range(N):
    words.append(input().strip())

words = set(words)
words = list(words)
words.sort(key=lambda x: (len(x), x))

sys.stdout.write("\n".join(words))
