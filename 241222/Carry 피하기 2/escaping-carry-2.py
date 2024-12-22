import sys

n = int(input())
a = []

for i in range(n):
    a.append( int(sys.stdin.readline().rstrip()) )

max_ans = -sys.maxsize

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if (a[i] % 10) + (a[j] % 10) + (a[k] % 10) >= 10:
                continue
            elif ((a[i] // 10) % 10) + ((a[j] // 10) % 10) + ((a[k] // 10) % 10) >= 10:
                continue
            elif ((a[i] // 100) % 10) + ((a[j] // 100) % 10) + ((a[k] // 100) % 10) >= 10:
                continue
            elif ((a[i] // 1000) % 10) + ((a[j] // 1000) % 10) + ((a[k] // 1000) % 10) >= 10:
                continue
            elif ((a[i] // 10000) % 10) + ((a[j] // 10000) % 10) + ((a[k] // 10000) % 10) >= 10:
                continue
            else:
                sum = a[i] + a[j] + a[k]
                max_ans = max(max_ans,sum)

print(max_ans)
