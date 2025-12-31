import math
import binascii

def integer_nth_root(n, r):

    if n < 0: return None
    if n == 0: return 0
    high = 1
    while high ** r < n:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** r < n:
            low = mid
        elif high > mid and mid ** r > n:
            high = mid
        else:
            return mid
    return mid if mid ** r == n else None

def solve():
    print("Reading files...")
    with open('./rsa_cube_root/ciphertext.hex', 'r') as f:
        c_hex = f.read().strip()
    
    with open('./rsa_cube_root/public.txt', 'r') as f:
        lines = f.readlines()
        
    n = 0
    e = 3
    for line in lines:
        if line.startswith('n'):
            n = int(line.split('=')[1].strip())
        if line.startswith('e'):
            e = int(line.split('=')[1].strip())
            
    c = int(c_hex, 16)
    
    print(f"e = {e}")
  
    print(f"c = {c}")
    

    
    m = integer_nth_root(c, 3)
    
    if m:
        print(f"Found integer cube root: {m}")
        try:
            m_bytes = binascii.unhexlify(hex(m)[2:])
            print(f"Recovered Message: {m_bytes.decode('utf-8')}")
        except Exception as err:
            print(f"Error decoding: {err}")
    else:
        print("Ciphertext is not a perfect cube (m^3 > n maybe?)")

if __name__ == "__main__":
    solve()
