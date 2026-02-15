N, M = map(int, input().split())
nums = list(map(int, input().split()))

closest = nums[0] + nums[1] + nums[2]
for n1 in nums :
  for n2 in nums :
    if n2 is not n1 :
      for n3 in nums:
        if n3 is not n1 and n3 is not n2 :
          if abs(M - (n1 + n2 + n3)) < abs(M - closest) and n1 + n2 + n3 <= M :
            closest = n1 + n2 + n3

print(closest)
