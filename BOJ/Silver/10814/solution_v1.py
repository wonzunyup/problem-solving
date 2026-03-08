N = int(input())
people = []
for _ in range(N):
    age, name = input().split()
    people.append([int(age), name])
people.sort(key=lambda x: x[0])

for i in range(N):
    print(people[i][0], people[i][1])
