import sys

arr = list(map(int, input().split()))

for a in range(1, max(arr) + 1):
    for b in range(a, max(arr) + 1):
        for c in range(b, max(arr) + 1):
            for d in range(c, max(arr) + 1):
                if a in arr and b in arr and c in arr and d in arr and \
                a + b in arr and b + c in arr and c + d in arr and d + a in arr and \
                a + c in arr and b + d in arr and \
                a + b + c in arr and a + c + d in arr and b + c + d in arr and \
                a + b + c + d in arr:
                    print(a, b, c, d)