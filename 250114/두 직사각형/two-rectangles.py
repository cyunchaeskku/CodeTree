import sys

x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

if x2 < a1:
    print("nonoverlapping")
else:
    if x1 > a2:
        print("nonoverlapping")
    else:
        if y1 > b2:
            print("nonoverlapping")
        else:
            if y2 < b2:
                print("nonoverlapping")
            else:
                print("overlapping")