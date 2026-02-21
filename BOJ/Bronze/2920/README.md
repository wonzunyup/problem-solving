# BOJ 2920 - 음계

## 1. 문제 유형
- 구현 / 배열 비교

## 2. 처음 접근
- 배열의 요소 하나하나 비교

## 3. 제출 코드
```python
import sys

input = sys.stdin.readline

melody = list(map(int, input().split()))

type = ""
if melody[0] <= melody[1]:
    type = "ascending"
    for i in range(1, 8):
        if melody[i - 1] <= melody[i]:
            continue
        else:
            type = "mixed"
            break
elif melody[0] >= melody[1]:
    type = "descending"
    for i in range(1, 8):
        if melody[i - 1] >= melody[i]:
            continue
        else:
            type = "mixed"
            break
print(type)
```

## 4. 개선 포인트
- 정확한 패턴이 아닌 1234569 와 같이 올라가기만 하면 ascending으로 판별 -> 논리 오류
- 직접 비교를 통한 최적화

## 5. 재작성 코드
```python
melody = list(map(int, input().split()))

if melody == [1,2,3,4,5,6,7,8]:
    print("ascending")
elif melody == [8,7,6,5,4,3,2,1]:
    print("descending")
else:
    print("mixed")
```

## 6. 배운점
- 조건 해석 실수 줄이기
- 때로는 직접 비교가 정답일 수가 있다

## 7. 풀이기록 
- 1차 풀이 : 2026-02-22
