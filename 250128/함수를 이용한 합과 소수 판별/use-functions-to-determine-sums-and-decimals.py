import sys
import math


def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 2):
            if n % i == 0:
                return False
        return True

def f(n):
    sum = 0 
    sum += n % 10
    n //= 10
    sum += n % 10
    n //= 10
    sum += n % 10

    if sum % 2 == 0:
        return True
    else:
        return False

a, b= map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if is_prime(i) and f(i):
        cnt += 1

print(cnt)