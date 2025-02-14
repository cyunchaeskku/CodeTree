def heapify(arr, n, i):
    largest = i
    l = i * 2
    r = i * 2 + 1

    if l <= n and arr[l] > arr[largest]:
        largest = l
    if r <= n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n , largest)
    

def heap_sort(arr, n):
    for i in range(n//2,0,-1):
        heapify(arr, n, i)
    
    for i in range(n,1,-1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr, i-1, 1)

n = int(input())
arr = [0]
ar = list(map(int, input().split()))
for v in ar:
    arr.append(v)

heap_sort(arr, len(arr) - 1)

for i, v in enumerate(arr):
    if i > 0:
        print(v, end=' ')

