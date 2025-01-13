import math

def fermat_factorization(N):
    a = math.ceil(math.sqrt(N))
    while True:
        b2 = a * a - N
        if b2 >= 0 and math.isqrt(b2)**2 == b2:  # Check if b^2 is non-negative and a perfect square
            b = int(math.sqrt(b2))
            p = a + b
            q = a - b
            return p, q
        a += 1


def fermat_large(n):
    a = math.isqrt(n) + 1  # Start with ceil(sqrt(n))
    while True:
        b2 = a * a - n
        if b2 >= 0:
            b = math.isqrt(b2)
            if b * b == b2:  # Check if b^2 is a perfect square
                p = a + b
                q = a - b
                return p, q
        a += 1  # Increment `a` carefully to minimize iterations