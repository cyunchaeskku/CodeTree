import sys

x1, x2, x3, x4 = map(int, input().split())

if x2 < x3:
    print("nonintersecting")
else:
    if x1 > x4:
        print("nonintersecting")
    else:
        print("intersecting")