n1, n2 = map(int, input().split())

a, b = n1, n2
while b:
    a, b = b, a % b

gcd = a
lcm = n1 * n2 // gcd

print(gcd)
print(lcm)
