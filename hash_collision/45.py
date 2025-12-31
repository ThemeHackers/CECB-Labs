import random
import string
import struct

def toy_hash(data: bytes) -> int:
    h = 0x9747b28c
    for b in data:
        h ^= b
        h *= 0x45d9f3b
        h &= 0xffffffff 
        
        
        left = (h << 13) & 0xffffffff
        right = (h >> 19) & 0xffffffff
        h = left | right
        
        h ^= 0x27100001
        h &= 0xffffffff
    return h

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def find_collision():
    seen_hashes = {}
    print("Starting Birthday Attack...")
    
    count = 0
    while True:
        s = generate_random_string(random.randint(5, 15))
        h = toy_hash(s.encode())
        
        if h in seen_hashes:
            if seen_hashes[h] != s:
                print(f"\nCollision found after {count} attempts!")
                print(f"Hash: 0x{h:08x}")
                print(f"String 1: {seen_hashes[h]}")
                print(f"String 2: {s}")
                return seen_hashes[h], s
        
        seen_hashes[h] = s
        count += 1
        if count % 10000 == 0:
            print(f"Attempts: {count}", end='\r')

if __name__ == "__main__":
    find_collision()
