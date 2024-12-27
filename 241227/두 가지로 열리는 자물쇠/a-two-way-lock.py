import sys

n = int(input())

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

cnt = 0


'''
min(i-a1, n-(i-a1))
'''

def get_min(i, a1):
    # return min(abs(i-a1),abs(n-(i-a1))) <= 2
    return abs(i - a1) <= 2 or abs(i - a1) >= n-2

for i in range(1,n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if ( get_min(i, a1) and get_min(j, b1) and get_min(k, c1) ) or ( get_min(i, a2) and get_min(j, b2) and get_min(k, c2) ):
                cnt += 1
    
            
            
print(cnt)