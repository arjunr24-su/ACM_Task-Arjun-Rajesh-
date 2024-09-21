# RSA Decryption using Chinese Remainder Theorem (CRT)

This project demonstrates how to decrypt a ciphertext encrypted with RSA using the Chinese Remainder Theorem (CRT).

## Steps to Decrypt

1. **Define the Public Exponent and Moduli**:
   - Identify the public exponent (e) and the moduli (n1, n2, n3) used in the RSA encryption.

2. **Calculate the Product of All Moduli**:
   - Compute the product of the moduli (N = n1 * n2 * n3).

3. **Compute Partial Products**:
   - For each modulus, calculate the partial product by dividing the total product (N) by that modulus (m1 = N/n1, m2 = N/n2, m3 = N/n3).

4. **Find Modular Inverses**:
   - Compute the modular inverse of each partial product with respect to its corresponding modulus.

5. **Combine Results Using CRT**:
   - Use the Chinese Remainder Theorem to combine the results from the different moduli. This involves summing the products of the ciphertexts, partial products, and their modular inverses, then taking the result modulo N.

6. **Extract the Plaintext**:
   - Since the public exponent (e) is 3, take the cube root of the combined result to obtain the plaintext.

## Decrypted Plaintext

    -42800643192346137370256222640646094543767840305996925