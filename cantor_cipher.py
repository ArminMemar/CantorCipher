# CantorCipher
import sys

# ========== Bitwise and Boolean Logic Utilities ==========
def str_to_bits(s):
    return ''.join(format(ord(c), '08b') for c in s)

def bits_to_str(bits):
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def xor_bits(a, b):
    return ''.join('1' if i != j else '0' for i, j in zip(a, b))

def rotate_bits(bits, n):
    n %= len(bits)
    return bits[n:] + bits[:n]

def permute_bits(bits):
    bits = list(bits)
    for i in range(0, len(bits) - 1, 2):
        bits[i], bits[i+1] = bits[i+1], bits[i]
    return ''.join(bits)

def boolean_mix(a, b):
    # Boolean logic-based nonlinear mixing
    return ''.join(str(((int(x) & ~int(y)) | (int(x) ^ int(y))) & 1) for x, y in zip(a, b))

# ========== Enhanced Bitwise Mixing ==========
def enhanced_bitwise_mix(key, rounds=5):
    mixed = key
    for r in range(rounds):
        rotated = rotate_bits(mixed, r + 1)
        mixed = boolean_mix(mixed, rotated)  # Replace XOR with boolean logic
        mixed = permute_bits(mixed)
    return mixed

# ========== Encryption Function ==========
def cantor_encrypt(message, key):
    msg_bits = str_to_bits(message)
    key_bits = str_to_bits(key)

    while len(key_bits) < len(msg_bits):
        key_bits += key_bits
    key_bits = key_bits[:len(msg_bits)]

    encrypted_bits = boolean_mix(msg_bits, key_bits)  # Boolean logic encryption
    return encrypted_bits

# ========== Decryption Function ==========
def cantor_decrypt(encrypted_bits, key):
    key_bits = str_to_bits(key)
    while len(key_bits) < len(encrypted_bits):
        key_bits += key_bits
    key_bits = key_bits[:len(encrypted_bits)]

    # In this symmetric version, decryption is same as encryption
    decrypted_bits = boolean_mix(encrypted_bits, key_bits)
    return bits_to_str(decrypted_bits)

# ========== Tag Generation ==========
def generate_tag(message, key, tag_length=128):
    msg_bits = str_to_bits(message)
    key_bits = str_to_bits(key)
    while len(key_bits) < len(msg_bits):
        key_bits += key_bits
    key_bits = key_bits[:len(msg_bits)]

    mixed_key = enhanced_bitwise_mix(key_bits)

    tag_bits = ''
    for i in range(tag_length):
        m_bit = msg_bits[i % len(msg_bits)]
        k_bit = mixed_key[i % len(mixed_key)]
        # Boolean condition for tag bit
        tag_bits += str(((int(m_bit) & ~int(k_bit)) | (int(m_bit) ^ int(k_bit))) & 1)

    return tag_bits

# ========== Command Line Interface ==========
def main():
    if len(sys.argv) < 4:
        print('Usage: python cantor_cipher.py <encrypt/decrypt> <"message/bits"> <"key">')
        return

    action = sys.argv[1]
    data = sys.argv[2]
    key = sys.argv[3]

    if action == "encrypt":
        encrypted = cantor_encrypt(data, key)
        tag = generate_tag(data, key)
        print("\n * Encrypted Message:")
        print(encrypted)
        print("\n * Key (bits):", str_to_bits(key))
        print("\n * Tag:", tag)

    elif action == "decrypt":
        decrypted = cantor_decrypt(data, key)
        print("\n * Decrypted Message:")
        print(decrypted)

    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()