def decrypt_rail_fence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
    
    dir_down = None
    row, col = 0, 0
    
    # Mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
            
    # Fill the '*' with characters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
                
    # Read the matrix
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        
        # Check direction
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
            
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
            
        if dir_down:
            row += 1
        else:
            row -= 1
            
    return("".join(result))

def solve():
    with open('./rail_fence_3rails/cipher.txt', 'r') as f:
        ciphertext = f.read().strip()
        
    print(f"Ciphertext: {ciphertext}")
    
    plaintext = decrypt_rail_fence(ciphertext, 3)
    print(f"Recovered Plaintext: {plaintext}")

if __name__ == "__main__":
    solve()
