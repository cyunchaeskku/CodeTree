import sys

MAX_NUM = 101

n = int(input())

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_dots = sys.maxsize

for i in range(MAX_NUM + 1):
    for j in range(MAX_NUM + 1):

        if i % 2 == 1 or j % 2 == 1:
            continue

        num_of_max_dots = 0

        one_quarter = 0
        two_quarter = 0
        three_quarter = 0
        four_quater = 0

        for x, y in points:
            if x > i and y > j:
                one_quarter += 1
            if x > i and y < j:
                two_quarter += 1
            if x < i and y < j:
                three_quarter += 1
            if x < i  and y > j:
                four_quater += 1
        num_of_max_dots = max(one_quarter, two_quarter, three_quarter, four_quater)
        # print(num_of_max_dots)

        min_dots = min(min_dots, num_of_max_dots)

print(min_dots)
