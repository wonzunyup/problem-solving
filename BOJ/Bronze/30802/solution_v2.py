N = int(input())

sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_packages = sum((s + T - 1) // T for s in sizes)
print(shirt_packages)
print(N // P, N % P)
