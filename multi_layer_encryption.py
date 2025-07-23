import base64

def apply_rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def xor_encrypt(text, key_char):
    return ''.join(chr(ord(c) ^ ord(key_char)) for c in text)

def reverse_text(text):
    return text[::-1]

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def encrypt_text(plaintext, xor_key):
    if len(xor_key) != 1:
        raise ValueError("XOR key must be a single ASCII character.")
    step1 = apply_rot13(plaintext)
    step2 = xor_encrypt(step1, xor_key)
    step3 = reverse_text(step2)
    step4 = base64_encode(step3)
    return step4

def main():
    plaintext = input("Enter plaintext: ")
    xor_key = input("Enter XOR key (1 ASCII character): ")
    try:
        result = encrypt_text(plaintext, xor_key)
        print("Encrypted Base64 Output:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()