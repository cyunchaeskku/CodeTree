n = int(input())

def func(n):
    res = 0
    for i in range(n+1):
        res += i

    return int(res// 10)

print(func(n))