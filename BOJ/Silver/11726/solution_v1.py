import sys

input = sys.stdin.readline

n = int(input())


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


cnt = 0
if n % 2 == 0:
    for i in range(0, n + 1, 2):
        two_by_one = i
        one_by_two = (n - i) // 2
        cnt += factorial(two_by_one + one_by_two) // (
            factorial(one_by_two) * factorial(two_by_one)
        )
else:
    for i in range(1, n + 1, 2):
        two_by_one = i
        one_by_two = (n - i) // 2
        cnt += factorial(two_by_one + one_by_two) // (
            factorial(one_by_two) * factorial(two_by_one)
        )
print(cnt % 10007)
