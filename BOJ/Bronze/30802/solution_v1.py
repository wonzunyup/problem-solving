N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

num = 0
for size in sizes : 
  if size % T == 0 :
    num += size // T
  else : num += size // T + 1
print(num)
print(N // P, N % P)
