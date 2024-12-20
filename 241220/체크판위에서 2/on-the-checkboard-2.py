r, c = map(int, input().split())

a = []

for i in range(r):
    a.append( list(input().split()) ) 

ans = 0

'''
0 = True
1 = False
'''
cur_color = -1

if a[0][0] == 'W':
    cur_color = True
else:
    cur_color = False

for i in range(1,r-1):
    for j in range(c-1):
        for k in range(i+1, r):
            for l in range(j+1, c):
                if a[i][j] != a[0][0] and a[k][l] == a[0][0] and k < r-1 and l < c-1 and a[k][l] != a[r-1][c-1]:
                    # print(a[i][j], a[k][l], i+1,j+1,k+1,l+1)
                    ans += 1

print(ans)
