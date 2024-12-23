import sys

n , k = map(int, input().split())
a= [0 for _ in range(200)]

max_ans = -sys.maxsize

for i in range(n):
    candy, index = map(int, input().split())
    a[index - 1] = candy

for i in range(0 + k ,200 - k):
    _sum = sum(a[i - k : i + k + 1])
    max_ans = max(max_ans, _sum)

print(max_ans)




'''
c=200
0~200

0 1 2 3 ... 196 197 198 199
'''