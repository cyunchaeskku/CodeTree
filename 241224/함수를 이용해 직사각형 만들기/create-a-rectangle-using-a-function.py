n, m = map(int, input().split())

def print_rect(n,m):
    for i in range(n):
        print("*" * m)

print(print_rect(n,m))