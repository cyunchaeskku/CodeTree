r, c = map(int, input().split())

a = []

for i in range(r):
    a.append( list(input().split()) ) 
ans = 0

for i in range(1,r-2):
    for j in range(1,c-2):
        for k in range(i+1, r-1):
            for l in range(j+1, c-1):
                if a[i][j] != a[0][0] and a[k][l] == a[0][0] and a[k][l] != a[r-1][c-1]:
                    # print(a[i][j], a[k][l], i+1,j+1,k+1,l+1)
                    ans += 1

print(ans)
