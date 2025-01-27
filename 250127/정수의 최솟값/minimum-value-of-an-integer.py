def func(*args):
    return min(args)

a,b,c = map(int, input().split())
print(func(a, b, c))