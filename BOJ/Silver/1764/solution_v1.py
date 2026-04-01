import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ns = set(input().rstrip() for _ in range(N))
ms = set(input().rstrip() for _ in range(N))

out = []
for person in ns:
    if person in ms:
        out.append(person)

out.sort()
sys.stdout.write(str(len(out)) + "\n")
sys.stdout.write("\n".join(out))
