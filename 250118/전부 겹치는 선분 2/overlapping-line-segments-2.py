import sys

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
# x1 = [seg[0] for seg in segments]
# x2 = [seg[1] for seg in segments]

# Write your code here!

for i in range(n):
    segments_copy = segments.copy()
    del segments_copy[i]
    x1 = [seg[0] for seg in segments_copy]
    x2 = [seg[1] for seg in segments_copy]
    max_x1 = max(x1)
    min_x2 = min(x2)

    if min_x2 >= max_x1:
        print("Yes")
        exit(0)
print("No")
