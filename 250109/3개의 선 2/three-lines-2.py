MAX_X = 10

n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0

for i in range(MAX_X + 1):
    for j in range(MAX_X + 1):
        for k in range(MAX_X + 1):

            success = True
            for x, y in points:
                if x == i or x == j or x == k:
                    continue

                success = False
            if success:
                ans = 1

            success = True
            for x,y in points:
                if x == i or x == j or y == k:
                    continue

                success = False
            if success:
                ans = 1

            success = True
            for x, y in points:
                if x == i or y == j or y == k:
                    continue

                success = False
            if success:
                ans = 1

            success = True
            for x, y in points:
                if y == i or y == j or y == k:
                    continue

                success = False
            if success:
                ans = 1
            
print(ans)