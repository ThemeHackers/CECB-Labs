import math
import binascii
import random


n = 98193368823922946385118684912528275664701535968983996254610274197465503989547
e = 65537
c_hex = "8aa19e1eb0360830c4292d2e724e1bee234fed1186b18c638c2928feb99dca68"
c = int(c_hex, 16)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n % 2 == 0: return 2
    
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1
    
    fn = lambda x: (x * x + c) % n
    
    while g == 1:
        x = fn(x)
        y = fn(fn(y))
        g = gcd(abs(x - y), n)
        
    return g

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def is_isqrt(n):
    if n < 0: return -1
    if n == 0: return 0
    x = int(math.isqrt(n))
    if (x*x) == n:
        return x
    return -1

def fermat_factor(n):
    a = math.isqrt(n)
    if a * a < n:
        a += 1
        
    count = 0
    while True:
        b2 = a * a - n
        b = is_isqrt(b2)
        if b >= 0:
            return (a - b, a + b)
        a += 1
        count += 1
        if count > 50000000: 
             return None

def solve():
    print(f"Factoring n = {n} ...")
    

    factors = fermat_factor(n)
    if factors:
         p, q = factors
    else:
         print("Fermat failed, falling back to Pollard's rho (might be slow)...")
         p = pollard_rho(n)
         q = n // p
    
    print(f"Found factors:\np = {p}\nq = {q}")
    

    if p * q != n:
        print("Error: Factorization failed!")
        return


    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    
    print(f"Private Key d = {d}")

    m = pow(c, d, n)
    

    m_hex = hex(m)[2:]
    try:
        m_bytes = binascii.unhexlify(m_hex)
        print(f"\nRecovered Message: {m_bytes.decode('utf-8')}")
    except Exception as err:
        print(f"Error decoding message: {err}")
        print(f"Raw hex: {m_hex}")

if __name__ == "__main__":
    solve()
