import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_to_name = {}
name_to_num = {}

for i in range(1, N + 1):
    name = input().rstrip()
    num_to_name[i] = name
    name_to_num[name] = str(i)

out = []
for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        out.append(num_to_name[int(question)])
    else:
        out.append(name_to_num[question])

sys.stdout.write("\n".join(out))
