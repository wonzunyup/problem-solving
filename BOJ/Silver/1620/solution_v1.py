import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_dict = {}
name_dict = {}

out = []
for i in range(N):
    name = input().rstrip()
    num_dict[i + 1] = name
    name_dict[name] = i + 1

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        out.append(num_dict[int(question)])
    else:
        out.append(str(name_dict[question]))

sys.stdout.write("\n".join(out))
