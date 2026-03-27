import sys

input = sys.stdin.readline

N = int(input())
words = set(input().strip() for _ in range(N))
words = list(words)
words.sort(key=lambda x: (len(x), x))

sys.stdout.write("\n".join(words))
