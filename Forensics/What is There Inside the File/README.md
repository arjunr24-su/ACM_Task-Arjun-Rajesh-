# Forensics Fun with Zip2John and John the Ripper

## Overview
This project demonstrates the process of extracting a password-protected zip file using `zip2john` and `John the Ripper` on Zorin OS. The final output is a base64 encoded message that decodes to "Forensics is fun".

## Steps

1. **Used zip2john on Zorin OS**: 
   - Added `zip2john` to the system path.
   - Generated a hash file from the zip file.

2. **Ran John the Ripper on the hash file**:
   - Ensured the zip file had proper permissions.
   - Successfully cracked the password: `softballs`.

3. **Extracted the zip using 7z**:
   - Extracted the contents of the zip file using the password obtained.
   - Found an unopenable `.pdf` file.

4. **Decoded the base64 message**:
   - The base64 encoded message `Rm9yZW5zaWNzIGlzIGZ1bg==` decodes to `Forensics is fun`.

## Tools Used
- **zip2john**
- **John the Ripper**
- **7z**

## Base64 Decoding
The base64 encoded string `Rm9yZW5zaWNzIGlzIGZ1bg==` translates to `Forensics is fun`.
