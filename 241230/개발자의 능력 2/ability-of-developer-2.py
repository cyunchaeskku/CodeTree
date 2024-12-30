import sys

a = list(map(int, input().split()))

'''
i, j, k, l
'''

min_ans = sys.maxsize

def get_diff(i,j,k,l):
    sum1 = a[i] + a[j]
    sum2 = a[k] + a[l]
    sum3 = sum(a) - sum1 - sum2
    return max(sum1, sum2, sum3) - min(sum1, sum2, sum3)


for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            for l in range(len(a)):
                if i != j and i != k and i != l and j != i and j != k and j != l and k != i and k != j and k != l:
                    # if get_diff(i,j,k,l) == 0:
                    #     print(a[i],a[j],a[k],a[l])
                    min_ans = min( get_diff(i,j,k,l), min_ans )


print(min_ans)