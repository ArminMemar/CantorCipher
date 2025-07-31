# CantorCipher

**CantorCipher** is a lightweight symmetric cryptographic algorithm grounded in mathematical principles—namely, **Cantor's diagonal argument**, **Boolean logic**, and **bitwise transformations**. Designed as an educational and experimental cipher, CantorCipher offers both encryption and message authentication capabilities through novel bit-mixing functions and authentication tag generation.


---

## Mathematical Design Rationale

CantorCipher draws conceptual inspiration from **Cantor’s diagonalization**, used here metaphorically to guarantee uniqueness and unpredictability in generated ciphertexts and tags. It integrates:

- Boolean logic operations: `AND`, `XOR`, `NOT`, and custom nonlinear functions
- Bit-level transformations: rotations, permutations, and Boolean mixing
- Enhanced avalanche through multi-round mixing
- Tag generation based on message–key correlation via Boolean rule-based diagonal mapping

The cipher operates entirely on binary strings derived from ASCII inputs, ensuring precise control over bit-level behavior.

---

## Algorithm Structure

1. **Bitwise Conversion**: Message and key are converted to binary.
2. **Key Expansion**: The key is cyclically extended to match message length.
3. **Enhanced Mixing**: Key undergoes multi-round Boolean mixing and permutation.
4. **Encryption**: Message is mixed with key using a custom Boolean formula.
5. **Tag Generation**: A fixed-length authentication tag is computed using a diagonalized, Boolean-based pattern across the message and mixed key.

Decryption reverses the Boolean mixing using the same symmetric logic.

---

## Features

- Lightweight and dependency-free
- Boolean-based nonlinear encryption
- Customizable number of mixing rounds
- Authentication tag generation for tamper detection
- Deterministic and reproducible behavior
- Easy-to-read Python implementation

---

## Usage
Encrypt a message
```bash
python cantor_cipher.py encrypt "Your message" "your secret key"
```

Decrypt a message
```bash
python cantor_cipher.py decrypt <encrypted bitstring> "your secret key"
```

Run test suite
```bash
python test_cantor_cipher.py
```
---

## Test Summary
The included test suite verifies the correctness and integrity of the cipher:

- Encryption–Decryption Consistency
- Avalanche Effect Test
- Authentication Tag Collision Resistance
- Tampering Detection

---

## Limitations and Future Work
CantorCipher is currently an educational and conceptual cipher:
- Not yet reviewed by cryptography experts or tested against formal attacks


Future improvements may include:
- Stronger tag generation algorithms
- Key schedule hardening
- Support for larger message blocks
- Formal proofs of security and diffusion metrics
- Hardware-optimized implementations

---

## License
This project is licensed under the MIT License.

---

## Contact
Project author and maintainer:

Armin Memar

GitHub: @ArminMemar

Email: [armin.memar.2007@gmail.com]

