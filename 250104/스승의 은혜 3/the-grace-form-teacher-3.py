import sys

n, b = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(n)]
p = [gift[0] for gift in gifts]
s = [gift[1] for gift in gifts]

# Write your code here!

ans = -sys.maxsize

for i in range(n):
    _p = p.copy()
    _s = s.copy()

    _p[i] = int(_p[i] / 2)

    total = []

    for j in range(n):
        total.append(_p[j] + _s[j])

    total.sort()
    price = 0
    people = 0

    for v in total:
        if price + v <= b:
            price += v
            people += 1
        else:
            break

    ans = max(people, ans)


    _p[i] = int(_p[i] * 2)

print(ans)