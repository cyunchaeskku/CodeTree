import sys

n = int(input())

ans = -sys.maxsize

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

for i in range(1, 4): # 돌을 1번부터 3번컵에 넣어보기
    stone = i
    score = 0
    for j in range(n):
        a, b, c = arr[j]
        if stone == a:
            stone = b
        elif stone == b:
            stone = a
        if c == stone:
            score += 1
    ans = max(ans, score)
print(ans)