# BOJ 1259 - 팰린드롬수

## 1. 문제 유형
- 구현

## 2. 처음 접근
- 인덱싱을 통해 문자열 뒤집어 비교

## 3. 제출 코드
```python
while(True) :
  num = input()
  if num == '0' : break
  temp = num[::-1]
  print("yes") if temp == num else print("no")
```

## 4. 개선 포인트
- 불필요한 변수 사용 제거

## 5. 재작성 코드
```python
while(True) :
  num = input()
  if num == '0' : break
  print("yes") if num[::-1] == num else print("no")
```

## 6. 배운점
- 코드 작성 후 한번 더 개선점 생각해보기

## 7. 풀이기록 
- 1차 풀이 : 2026-02-15
- 2차 풀이 : 2026-02-24
