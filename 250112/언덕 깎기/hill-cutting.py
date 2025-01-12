import sys

MAX_HEIGHT = 100

n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

ans = sys.maxsize

for i in range(MAX_HEIGHT + 1): # i: 가장 낮은 언덕의 높이가 i. 다른 모든 언덕의 높이는 [i,i+17] 이어야 함
    cost = 0

    for j in range(n):
        if arr[j] < i:
            cost += (i - arr[j]) ** 2
        if arr[j] > i + 17:
            cost += (arr[j] - i - 17) ** 2

    ans = min(ans, cost)

print(ans)
