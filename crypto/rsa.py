import math
from grwnapy.crypto.math import get_sqr_root

rsa_e = 65537

def fermat_factorization(N):
    """ Factorize n using fermat """
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
    """ Factorize large n using fermat """
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

def rabin_even(ct: int, e: int, n: int):
    """ Rabin-like decryption for even public exponent\n 
        ct: ciphertext\n
        e: public exponent\n
        n: modulus """
    roots = get_sqr_root(ct,n, errors="no")
    iteration = int(math.log2(e)) - 1
    for i in range(iteration):
        new_roots = []
        for root in roots:
            try:
                temproot = get_sqr_root(root, n, errors="no")
                new_roots.append(temproot[0])
                new_roots.append(temproot[1])
            except:
                continue
        roots = new_roots.copy()
    return roots