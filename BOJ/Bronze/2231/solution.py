N = int(input())

generator = 0
for i in range(N, 0, -1) :
  sum = i
  temp = str(i)
  for j in range(len(temp)) :
    sum += int(temp[len(temp) - 1 - j])
  if sum == N : generator = i
print(generator)
