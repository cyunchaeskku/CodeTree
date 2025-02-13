def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i + 1

def quick_sort(arr, lo, hi):
    if lo < hi:
        pos = partition(arr, lo, hi)

        quick_sort(arr, lo, pos - 1)
        quick_sort(arr, pos + 1, hi)

n  = int(input())
arr = list(map(int, input().split()))

quick_sort(arr,0,len(arr)-1)

for v in arr:
    print(v, end=' ')