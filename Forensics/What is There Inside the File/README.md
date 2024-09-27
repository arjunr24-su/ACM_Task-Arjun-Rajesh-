# Forensics Fun with Python Zip Cracker

## Overview

This project demonstrates the process of extracting a password-protected ZIP file using a custom Python script. The final output is a base64 encoded message that decodes to "Forensics is fun".

## Steps

1. **Used a Custom Python Script:**
   - Developed a Python script that utilizes `pyzipper` to attempt to crack the ZIP file's password using a wordlist.
   - The wordlist used is `rockyou.txt`, which contains a vast collection of common passwords.

2. **Ran the Python Script:**
   - Ensured the ZIP file had proper permissions.
   - Successfully cracked the password: `softball3`.
   - Extracted the contents of the ZIP file using the obtained password.

3. **Encountered an Unopenable PDF:**
   - Found an unopenable `.pdf` file among the extracted contents.

4. **Decoded the Base64 Message:**
   - The base64 encoded message `Rm9yZW5zaWNzIGlzIGZ1bg==` decodes to `Forensics is fun`.

## Tools Used

- Python with `pyzipper`
- `rockyou.txt` (Wordlist)
- Base64 Decoder

## Base64 Decoding

The base64 encoded string `Rm9yZW5zaWNzIGlzIGZ1bg==` translates to `Forensics is fun`.
