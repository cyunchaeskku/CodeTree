import sys

min_ans = sys.maxsize

n = int(input())

a= []

for i in range(n):
    a.append( list(map(int,input().split())) )

# length = abs( a[j][0] - a[j-1][0] ) + abs( a[j][1] - a[j-1][1] )

for i in range(1, n-1):
    temp_list = a.copy()
    del temp_list[i]
    length = 0
    for j in range(1, len(temp_list)):
        length += abs( temp_list[j][0] - temp_list[j-1][0] ) + abs( temp_list[j][1] - temp_list[j-1][1] )
    if length < min_ans:
        min_ans = length


print(min_ans)            