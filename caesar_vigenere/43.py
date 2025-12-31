import string

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
           
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            value = (ord(char) - ascii_offset)
            key_val = (ord(key[key_index % key_length].upper()) - 65)
            
          
            decrypted_val = (value - key_val) % 26
            plaintext += chr(decrypted_val + ascii_offset)
            key_index += 1
        else:
            plaintext += char
    return plaintext

def solve():

    try:
        with open('./caesar_vigenere/caesar.txt', 'r') as f:
            caesar_cipher = f.read().strip()
        
        print(f"Caesar Cipher: {caesar_cipher}")
        print("-" * 20)
        
        found_caesar = ""
        for shift in range(1, 26):
            decrypted = caesar_decrypt(caesar_cipher, shift)
        
            if "FLAG" in decrypted or "CAESAR" in decrypted:
                print(f"Shift {shift}: {decrypted}  <-- LIKELY_CANDIDATE")
                found_caesar = decrypted
            
    except Exception as e:
        print(f"Error reading/processing Caesar: {e}")

    print("\n" + "=" * 20 + "\n")

    try:
        with open('./caesar_vigenere/vigenere.txt', 'r') as f:
            vigenere_cipher = f.read().strip()
            
        key = "REDTEAM"
        print(f"Vigenère Cipher: {vigenere_cipher}")
        print(f"Key: {key}")
        print("-" * 20)
        
        vigenere_plaintext = vigenere_decrypt(vigenere_cipher, key)
        print(f"Vigenère Plaintext: {vigenere_plaintext}")
        
    except Exception as e:
        print(f"Error reading/processing Vigenère: {e}")

if __name__ == "__main__":
    solve()
