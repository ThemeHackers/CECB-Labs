import json
import binascii

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def solve():
    with open('./rc4/rc4.json', 'r') as f:
        data = json.load(f)
    
    c1_hex = data['ciphertext_known_hex']
    p1 = data['known_plaintext_ascii']
    c2_hex = data['ciphertext_secret_hex']
    
    
    c1 = binascii.unhexlify(c1_hex)
    c2 = binascii.unhexlify(c2_hex)
    p1_bytes = p1.encode('utf-8')
    
    
    keystream = xor_bytes(c1, p1_bytes)
    
    print(f"Recovered Keystream (Hex): {binascii.hexlify(keystream).decode()}")

    
    p2 = xor_bytes(c2, keystream)
    
    print(f"\nSecret Plaintext (Hex): {binascii.hexlify(p2).decode()}")
    try:
        print(f"Secret Plaintext (ASCII): {p2.decode('utf-8')}")
    except UnicodeDecodeError:
        print("Could not decode as UTF-8")

if __name__ == "__main__":
    solve()
