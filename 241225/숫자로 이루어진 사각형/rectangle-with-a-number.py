n = int(input())

def print_square(n):
    cnt = 1
    for j in range(n):
        for i in range(n):
            print(cnt, end = " ")
            cnt += 1
            if cnt > 9:
                cnt = 1
        print()

print_square(n)