import json

def solve_gcm_nonce_reuse(file_path):

    with open(file_path, 'r') as f:
        data = json.load(f)


    p1_ascii = data['known_plaintext_ascii']
    c1_hex = data['ciphertext1_hex']
    c2_hex = data['ciphertext2_hex']


    c1 = bytes.fromhex(c1_hex)
    c2 = bytes.fromhex(c2_hex)
    p1 = p1_ascii.encode()

    keystream = bytes([c1[i] ^ p1[i] for i in range(len(p1))])

    p2_bytes = bytes([c2[i] ^ keystream[i] for i in range(len(c2))])

    return p2_bytes.decode('ascii')

try:
    recovered_message = solve_gcm_nonce_reuse('./aes256_gcm_bad/gcm.json')
    print(f"Recovered Message: {recovered_message}")
except Exception as e:
    print(f"Error: {e}")