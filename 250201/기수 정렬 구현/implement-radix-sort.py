import sys

n = int(input())
a = list(map(int, input().split()))

def get_posth_digit(pos, n):
    for i in range(pos):
        n //= 10
    return n % 10


def radix_sort(k, a):
    for pos in range(k):
        arr_new = [[] for _ in range(10)]
        for i in range(len(a)):
            digit = get_posth_digit(pos, a[i])
            arr_new[digit].append(a[i])

        store_arr = []
        for i in range(10):
            for j in range(len(arr_new[i])):
                store_arr.append(arr_new[i][j])

        a = store_arr
    return a

for v in radix_sort(6, a):
    print(v,end=' ')