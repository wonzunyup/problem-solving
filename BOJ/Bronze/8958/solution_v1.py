N = int(input())

for _ in range(N):
    result = input().strip()
    score = 0
    temp = 0
    for s in result:
        if s == "O":
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)
