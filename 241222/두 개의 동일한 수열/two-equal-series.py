n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for _a, _b in zip(a, b):
    if _a != _b:
        print("No")
        exit(0)

print("Yes")