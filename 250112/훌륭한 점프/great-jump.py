import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))

min_val = min(a)
max_val = max(a)

ans = sys.maxsize

def is_possible(max_val):
    available_indicies = []
    
    for i in range(n):
        if a[i] <= max_val:
            available_indicies.append(i)

    arr_size = len(available_indicies)

    if arr_size == 1:
        return False

    if 0 not in available_indicies:
        return False

    for i in range(1, arr_size):
        if available_indicies[i] - available_indicies[i-1] > k:
            return False

    return True


for i in range(1, max_val+1):
    if is_possible(i):
        ans = min(ans, i)

print(ans)