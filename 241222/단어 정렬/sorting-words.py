n = int(input())

a = []

for i in range(n):
    a.append(input().rstrip())

a.sort()

for v in a:
    print(v)