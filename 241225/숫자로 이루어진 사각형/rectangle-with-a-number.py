n = int(input())

def print_square(n):
    cnt = 1
    for i in range(n):
        print(cnt, end = " ")
        cnt += 1
    print()

print_square(n)