import math

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b):
    m = 26
    a_inv = modinv(a, m)
    if a_inv is None:
        return None
    
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - 65
            x = (a_inv * (y - b)) % m
            plaintext.append(chr(x + 65))
        else:
            plaintext.append(char)
    return "".join(plaintext)

def solve():
    with open('./affine_cipher/cipher.txt', 'r') as f:
        ciphertext = f.read().strip()

    print(f"Ciphertext: {ciphertext}")
    print("-" * 30)

    
    valid_a = [i for i in range(1, 26) if math.gcd(i, 26) == 1]
    
    for a in valid_a:
        for b in range(26):
            pt = affine_decrypt(ciphertext, a, b)
            
            if "AFFINE" in pt or "FLAG" in pt:
                print(f"Found candidate (a={a}, b={b}): {pt}")

if __name__ == "__main__":
    solve()
