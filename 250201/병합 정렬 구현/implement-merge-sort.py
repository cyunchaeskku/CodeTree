import sys

MAX_N = 100_000

n = int(input())
a = list(map(int, input().split()))

def merge_sort(arr, lo, hi):
    mid = (lo+hi) // 2
    if lo < hi:
        merge_sort(arr, lo, mid)
        merge_sort(arr, mid+1, hi)
        arr = merge(arr, lo, mid, hi)

        return arr
    
merged_arr = [0 for _ in range(MAX_N + 1)]

def merge(arr, lo, mid, hi):
    i = lo
    j = mid + 1
    k = lo

    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            merged_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arr[j]
            k += 1
            j += 1
    
    while i <= mid:
        merged_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= hi:
        merged_arr[k] = arr[j]
        k += 1
        j += 1

    for k in range(lo, hi+1):
        arr[k] = merged_arr[k]

    return arr

a = merge_sort(a, 0, n-1)

for v in a:
    print(v, end= ' ')