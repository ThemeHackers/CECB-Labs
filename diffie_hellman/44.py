import json

def solve():
    try:
       
        try:
            with open('./diffie_hellman/params.json', 'r') as f:
                params = json.load(f)
            p = int(params['p_dec'])
            g = int(params['g_dec'])
            A = int(params['A_dec'])
            B = int(params['B_dec'])
        except FileNotFoundError:

            print("params.json not found, using hardcoded values.")
            p = 1222023965506290853
            g = 5
            A = 528522703702450282
            B = 566132874237330265
        
        print(f"p = {p}")
        print(f"g = {g}")
        print(f"A = {A}")
        print(f"B = {B}")
        
       
        print("Brute-forcing 'a' (Alice's private key)...")
        limit = 2**22 + 100 
        
        a_found = None
        for x in range(1, limit):
            if pow(g, x, p) == A:
                print(f"Found a! a = {x}")
                a_found = x
                break
        
        if not a_found:
            print("Failed to find 'a' within the limit.")
            return

        shared_secret = pow(B, a_found, p)
        print(f"Shared Secret (decimal): {shared_secret}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    solve()
