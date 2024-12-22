n = int(input())

a = list(map(int, input().split()))

a.sort()

for v in a:
    print(v, end=' ')
print()

a_rev = list(reversed(a))
for v in a_rev:
    print(v, end=' ')
print()
