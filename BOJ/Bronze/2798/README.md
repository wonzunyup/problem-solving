# BOJ 2798 블랙잭

## 1. 문제 유형
- 브루트포스

## 2. 처음 접근
- 받은 숫자들의 조합의 합을 통해 근사값 계산

## 3. 제출 코드
```python
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
```

## 4. 개선 포인트
- is not 사용 오류 : 값 비교 X, 객체 동일성 검사이브로 오작동 가능성 -> 인덱스를 통한 접근
- 중복 조합 검사가 불필요하게 많이 진행되어 비효율적 -> 인덱스 비교를 통해 효율성 증대
- 초기값 오류 가능성 : 초기값이 조건을 만족하지 않을 가능성

## 5. 재작성 코드
```python
N, M = map(int, input().split())
nums = list(map(int, input().split()))

closest = 0
for i in range(N) :
  for j in range(i + 1, N) :
    for k in range(j + 1, N) :
      total = nums[i] + nums[j] + nums[k]
      if total <= M and total > closest : closest = total

print(closest)
```

## 6. 배운점
- 중복으로 검사하는 case에 대한 검토 필요
- 파이썬에 아직 익숙치 않아서 언어 자체에 대한 이해 필요
- 초기값 세팅의 중요성

## 7. 풀이기록 
- 1차 풀이 : 2026-02-15
