import math

def is_prime_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

a, b= map(int, input().split())
ans = 0

for i in range(a, b+1):
    if is_prime_number(i):
        ans += i
print(ans)