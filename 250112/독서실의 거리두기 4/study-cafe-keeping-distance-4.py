import sys

n = int(input())
arr = list(map(int, list(input().strip())))

ans = -sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        if arr[i] == 1 or arr[j] == 1:
            continue
        dist = sys.maxsize
        ar = arr.copy()
        ar[i] = 1
        ar[j] = 1

        one_indicies = []
        for k in range(n):
            if ar[k] == 1:
                one_indicies.append(k)

        for k in range(len(one_indicies) - 1):
            dist = min(dist, abs(one_indicies[k] - one_indicies[k+1]))

        ans = max(dist, ans)

print(ans)