import pyzipper
import os

def crack_zip(zip_filepath, wordlist_filepath):
    if not os.path.exists(zip_filepath):
        print(f"Error: Zip file '{zip_filepath}' not found.")
        return
    if not os.path.exists(wordlist_filepath):
        print(f"Error: Wordlist file '{wordlist_filepath}' not found.")
        return

    with open(wordlist_filepath, 'r') as wordlist:
        passwords = wordlist.readlines()

    passwords = [password.strip() for password in passwords]

    with pyzipper.AESZipFile(zip_filepath) as zip_file:
        for password in passwords:
            try:
                zip_file.pwd = password.encode('utf-8')
                zip_file.testzip()
                print(f"Password found: {password}")
                return password
            except (RuntimeError, pyzipper.BadZipFile, pyzipper.LargeZipFile):
                continue

    print("Password not found in the wordlist.")
    return None

zip_filepath = '/home/arjun_rajesh/Downloads/Trybreakingme.zip'
wordlist_filepath = '/home/arjun_rajesh/Downloads/rockyou.txt'

crack_zip(zip_filepath, wordlist_filepath)
