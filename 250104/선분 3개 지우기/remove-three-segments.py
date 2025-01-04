import sys

n = int(input())
l = []
r = []
lines = []

max_val = -sys.maxsize
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)
    max_val = max(max_val, right)
    lines.append((left, right))

# Write your code here!

ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            lines_copy = lines.copy()

            lines_copy[i] = (-1,-1)
            lines_copy[j] = (-1,-1)
            lines_copy[k] = (-1,-1)

            coordinates = [0 for _ in range(max_val+1)] #

            for l in range(n):
                left, right = lines_copy[l]
                if left == -1 and right == -1:
                    continue
                for p in range(left, right+1):
                    coordinates[p] += 1
            answer = True
            for p in range(max_val + 1):
                if coordinates[p] > 1:
                    answer = False
            if answer:
                ans +=1

print(ans)