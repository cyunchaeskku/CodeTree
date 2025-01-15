import sys

n = int(input())

a = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_val = sys.maxsize
max_val = -sys.maxsize

for i in range(n):
    min_val = min(min_val, min(a[i]))
    max_val = max(max_val, max(a[i]))

arr = [0 for _ in range(101)]

for i in range(n):
    for j in range(a[i][0], a[i][1] + 1):
        arr[j] += 1

# print(arr)
success = False
for v in arr:
    if v >= n:
        success = True
        break

if success:
    print("Yes")
else:
    print("No")