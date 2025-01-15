a, b = map(int, input().split())
c, d = map(int, input().split())

min_val = min(a, c)
max_val = max(b, d)

# print(max_val - min_val)

ans = 0
if b < c or d < a:
    print( (b -a) + (d-c) )
else:
    print(max_val - min_val)