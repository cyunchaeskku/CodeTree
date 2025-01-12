import sys

arr = list(map(int, input().split()))



for a in range(min(arr), max(arr) + 1):
    for b in range(a, max(arr) + 1):
        for c in range(b, max(arr) + 1):
            for d in range(c, max(arr) + 1):
                ar = arr.copy()
                # if a in arr and b in arr and c in arr and d in arr and \
                # a + b in arr and b + c in arr and c + d in arr and d + a in arr and \
                # a + c in arr and b + d in arr and \
                # a + b + c in arr and  a + b + d in arr and a + c + d in arr and b + c + d in arr and \
                # a + b + c + d in arr:
                #     print(a, b, c, d)
                if a in ar:
                    ar.remove(a)
                if b in ar:
                    ar.remove(b)
                if c in ar:
                    ar.remove(c)
                if d in ar:
                    ar.remove(d)
                if a+b in ar:
                    ar.remove(a+b)
                if b+c in ar:
                    ar.remove(b+c)
                if c+d in ar:
                    ar.remove(c+d)
                if d+a in ar:
                    ar.remove(d+a)
                if a+c in ar:
                    ar.remove(a+c)
                if b+d in ar:
                    ar.remove(b+d)
                if a+b+c in ar:
                    ar.remove(a+b+c)
                if a+b+d in ar:
                    ar.remove(a+b+d)
                if a+c+d in ar:
                    ar.remove(a+c+d)
                if b+c+d in ar:
                    ar.remove(b+c+d)
                if a+b+c+d in ar:
                    ar.remove(a+b+c+d)
                if len(ar) == 0:
                    print(a,b,c,d)
