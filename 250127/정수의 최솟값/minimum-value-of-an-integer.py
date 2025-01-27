def func(*args):
    return sum(args)

a,b,c = map(int, input().split())
print(func(a, b, c))