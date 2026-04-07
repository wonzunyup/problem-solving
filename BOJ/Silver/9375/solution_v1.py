from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

out = []
for _ in range(T):
    n = int(input())
    clothes = defaultdict(list)

    for _ in range(n):
        name, kind = input().split()
        clothes[kind].append(name)

    result = 1
    for clothe in clothes.values():
        result *= len(clothe) + 1
    out.append(str(result - 1))

sys.stdout.write("\n".join(out))
