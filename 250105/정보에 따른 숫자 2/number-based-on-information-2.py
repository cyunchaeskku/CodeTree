import sys

t, a, b = map(int, input().split())

arr = []
coordinates = []
dic = {}

for i in range(t):
    alphabet, num = input().split()
    coordinates.append(int(num))
    dic[int(num)] = alphabet
    arr.append((alphabet, int(num)))

coordinates.sort()

def find_closest_coordinate(k, char):
    ans = -1
    min_val = sys.maxsize
    for i in range(len(coordinates)):
        if dic[coordinates[i]] == char:
            if min_val > abs(k-coordinates[i]):
                min_val = abs(k-coordinates[i])
                ans = coordinates[i]
    return min_val

cnt =0
for x in range(a, b+1):
    if find_closest_coordinate(x, 'S') <= find_closest_coordinate(x, 'N'):
        cnt += 1

print(cnt)

