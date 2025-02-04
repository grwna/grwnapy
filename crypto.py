from Crypto.Util.number import *
import base64
# List of functions
# gcd
# egcd
# binexp (slower than pow())
# modinv
# isQuadrRes
# findSqrRoot

# ===== IMPORTABLE =====
# ++++++++++ Booleans ++++++++++
def isCoprime(a,b):
    return gcd(a,b) == 1
def isQuadrRes(n : int, p : int) -> bool:
    return pow(n,(p-1)//2,p) == 1 or pow(n,(p-1)//2,p) == 0 

# ++++++++++ Calculations ++++++++++
def gcd(a : int,b : int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def egcd(a : int, b : int) -> tuple[int, int, int]:
    x, y = 0, 1   # Coefficients for a
    u, v = 1, 0   # Coefficients for b

    while a != 0:
        q = b // a      # Quotient
        a, b = b % a, a
        x, u = u - q * x, x
        y, v = v - q * y, y

    return b, v, u  # gcd, x, y for ax + by = gcd

def binexp(a : int, b : int, p : int) -> int:      # binary exponentiation
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % p
        a = (a*a) % p
        b = b // 2
    return res

def modinv(a : int, p : int):    # Calculates the Modular Inverse
    # METHOD 1 (Slower)
    # g, x, y = egcd(a,p)
    # if x < 0:
    #     x += p

    # METHOD 2: Fermat
    return pow(a, -1, p)


def findSqrRoot(n : int, p : int) -> tuple[int,int]:   # Uses Tonelli-Shanks
    if not isQuadrRes(n,p):
        print("Value not quadratic residue, Square root does not exist")
        return
    
    if n % p == 0:
        return 0
    elif p % 4 == 3:
        return pow(n, (p+1)//4, p)

    # Find z quadratic non residue
    z = 2
    while isQuadrRes(z,p):
        z += 1

    # Find Q
    Q = (p-1)
    S = 0
    while Q % 2 == 0:
        Q //= 2
        S += 1
    
    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q+1)//2, p)
    if t == 0:
        return 0;
    else:
        while t != 1:
            i = 0
            temp = t
            while temp != 1:
                temp = pow(temp, 2, p)
                i += 1

            b = pow(c,pow(2,M-i-1),p)
            M = i
            c = pow(b, 2, p)
            t = (t * c) % p
            R = (R * b) % p
        return R , p-R    

def crt(a : list[int], p : list[int]) -> tuple[int,int]:
    y = []
    M = [] 
    newP = 1
    x = 0
    # Initialize M & y
    for i in range(len(a)):
        Mtemp = 1
        for j in range(len(a)):
            if j != i:
                Mtemp *= p[j]
        M.append(Mtemp)
        y.append(modinv(M[i],p[i]))
    # Calculate the CRT
        newP *= p[i]
        x += a[i] * M[i] * y[i]
    return (x % newP,newP)

# ======== Galois Theory =================
def get_generator(p: int) -> int:
    """ generate a primitive number g for generator from modulus p"""
    factors = list(set(factor(p-1, mode="primefac")))
    for g in range(2,p):
        if all(pow(g, (p-1)//q,p) != 1 for q in factors):
            return g
    print("Generator not found")
    return None


# ======== Shortener =================
# Shortens the syntax of other libraries for most used scenarios
def factor(number: int, mode="factordb") -> list:
    """ Return the factors of a number according to FactorDB """

    if mode == "factordb":
        from factordb.factordb import FactorDB
        f = FactorDB(number)
        f.connect()
        factors = f.get_factor_list()
    elif mode == "primefac":
        from primefac import primefac
        factors = primefac(number)
    else:
        print("Mode used is invalid!")
        return 0

    return factors

def root(base: int, exponent: int) -> tuple:
    """ Takes the root of base (base ** 1/exponent) \n
        Returns (root, is_exact)"""
    from gmpy2 import gmpy2
    return gmpy2.iroot(base, exponent)


# ======== List and Strings ==========
# Takes a string, and split it into equal (if possible) lengths of n
def splitByN(text : str, n : int) -> list[str]:
    return [text[i:i + n] for i in range(0, len(text), n)]

def b64_to_long(b64_string):
    decoded_bytes = base64.b64decode(b64_string)
    long_int = bytes_to_long(decoded_bytes)
    return long_int

def long_to_b64(long_int):
    byte_data = long_to_bytes(long_int)
    b64_string = base64.b64encode(byte_data)
    return b64_string
# ===== NON-IMPORTABLE =====