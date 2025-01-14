import sys

MAX_A = 10_000

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize

for i in range(MAX_A):  # 리스트 안 최솟값이 i. 그럼 최댓값은 i + k 이하여야 함.
    cost = 0
    ar = arr.copy()

    for j in range(n):
        if ar[j] < i:
            # ar[j] += (i - ar[j])
            cost += abs(i - ar[j])
            # print(i - ar[j])
        if ar[j] > i + k:
            # ar[j] -= (ar[j] - i - k)
            cost += abs(ar[j] - i - k)
            # print(ar[j] - i - k)
   
    ans = min(ans, cost)
    
print(ans)