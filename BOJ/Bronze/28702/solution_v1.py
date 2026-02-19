import sys
input = sys.stdin.readline

strings = [input().strip() for _ in range(3)]
pos = 0
for i in range(3):
    if strings[i] == "Fizz" or strings[i] == "Buzz" or strings[i] == "FizzBuzz":
        continue
    else:
        pos = i

num = int(strings[pos]) + 3 - pos
if num % 3 == 0:
    if num % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if num % 5 == 0:
        print("Buzz")
    else:
        print(num)
