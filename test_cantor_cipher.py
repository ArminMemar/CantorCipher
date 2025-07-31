import cantor_cipher


def test_encrypt_decrypt():
    print("Test: Encryption-Decryption Consistency")
    message = "Hello, CantorCipher!"
    key = "securekey123"

    encrypted = cantor_cipher.cantor_encrypt(message, key)
    decrypted = cantor_cipher.cantor_decrypt(encrypted, key)

    assert decrypted == message, "Decryption failed!"
    print("* Passed")

def test_avalanche_effect():
    print("\nTest: Avalanche Effect")
    message = "AvalancheTest"
    key = "key123456"

    encrypted = cantor_cipher.cantor_encrypt(message, key)

    # Flip one bit in message and encrypt again
    msg_bits = ''.join(format(ord(c), '08b') for c in message)
    flipped_bits = list(msg_bits)
    flipped_bits[5] = '1' if flipped_bits[5] == '0' else '0'
    flipped_msg = ''.join(chr(int(''.join(flipped_bits[i:i+8]), 2)) for i in range(0, len(flipped_bits), 8))

    encrypted_flipped = cantor_cipher.cantor_encrypt(flipped_msg, key)

    diff = sum(b1 != b2 for b1, b2 in zip(encrypted, encrypted_flipped))
    total_bits = len(encrypted)
    print(f"Bits different after flipping 1 bit in message: {diff}/{total_bits} ({diff/total_bits*100:.2f}%)")

def test_tag_consistency():
    print("\nTest: Tag Consistency and Collision Check")
    message1 = "TestMessageOne"
    message2 = "TestMessageTwo"
    key = "key123456"

    tag1 = cantor_cipher.generate_tag(message1, key)
    tag2 = cantor_cipher.generate_tag(message1, key)  # same message and key
    tag3 = cantor_cipher.generate_tag(message2, key)

    assert tag1 == tag2, "Tags should match for same input!"
    assert tag1 != tag3, "Tags should differ for different messages!"

    print("* Passed")

def test_tampering_detection():
    print("\nTest: Tampering Detection")
    message = "OriginalMessage"
    key = "key123456"

    encrypted = cantor_cipher.cantor_encrypt(message, key)
    tag = cantor_cipher.generate_tag(message, key)

    # Tamper message
    tampered_msg = "OriginalMessagf"
    tampered_tag = cantor_cipher.generate_tag(tampered_msg, key)

    if tag != tampered_tag:
        print("* Tampering detected!")
    else:
        print("* Tampering NOT detected!")

def run_all_tests():
    test_encrypt_decrypt()
    test_avalanche_effect()
    test_tag_consistency()
    test_tampering_detection()

if __name__ == "__main__":
    run_all_tests()
