import base64

def decode_base64_layers(file_path):
    with open(file_path, 'r') as f:
        current_text = f.read().strip()
    
    layer = 0
    while True:
        try:
            decoded_bytes = base64.b64decode(current_text, validate=True)
            decoded_text = decoded_bytes.decode('utf-8')
            current_text = decoded_text
            layer += 1
        except Exception:
            
            break
            
    print(f"Decoded {layer} layers.")
    return current_text

try:
    decoded_message = decode_base64_layers('./base64_layers/enc.txt')
    print(f"Decoded Message (Raw): {decoded_message}")
    print(f"Decoded Message (Reversed): {decoded_message[::-1]}")
except Exception as e:
    print(f"Error: {e}")