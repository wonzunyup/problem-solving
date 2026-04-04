import sys

input = sys.stdin.readline

N, M = map(int, input().split())
people1 = set(input().rstrip() for _ in range(N))
people2 = set(input().rstrip() for _ in range(M))

result = sorted(people1 & people2)
print(len(result))
sys.stdout.write("\n".join(result))
