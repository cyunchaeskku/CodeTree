import sys

'''
한 변은 x축에 평행
다른 한 변은 y축에 평행
최대 넓이에 2를 곱한 값 구하기
만약 그러한 삼각형이 없다면 0 출력
x축과 평행: y값이 동일한 두 점 (x값은 다르고)
y축과 평행: x값이 동일한 두 점 (y값은 다르고)
'''

n = int(input())
a = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = -sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = a[i]
            x2, y2 = a[j]
            x3, y3 = a[k]

            x_parallel = False
            y_parallel = False

            if y1 == y2 or y2 == y3 or y3 == y1:
                x_parallel = True
            if x1 == x2 or x2 == x3 or x3 == x1:
                y_parallel = True

            if x_parallel and y_parallel:
                val = abs( (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3) )
                ans = max(ans, val)

print(ans)
    