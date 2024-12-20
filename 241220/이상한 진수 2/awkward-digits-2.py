import sys

string = input().rstrip()

ans_max = -sys.maxsize

a = list(string)

# print( ''.join(a))

for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
    else:
        a[i] = '0'
    
    if ans_max < int ( ''.join(a), 2 ):
        ans_max = int ( ''.join(a), 2 )

    if a[i] == '0':
        a[i] = '1'
    else:
        a[i] = '0'
    
print(ans_max)