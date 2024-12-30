import sys

min_ans = sys.maxsize

a = list(map(int, input().split()))

def get_diff(i,j,k):
    sum1 = a[i] + a[j]
    sum2 = a[k]
    sum3 = sum(a) - sum1 - sum2

    return max(sum1, sum2, sum3) - min(sum1, sum2, sum3)


for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if i == j or j == k or k == i:
                continue

            if a[i] + a[j] == a[k] or a[k] == sum(a) - (a[i] + a[j]) -  a[k] or sum(a) - (a[i] + a[j]) -  a[k] == a[i] + a[j]:
                continue

            min_ans = min(min_ans, get_diff(i,j,k))

if min_ans > 5000:
    print(-1)
else:
    print(min_ans)