import os
import pyzipper

# Path to your ZIP file
zip_file_path = r'C:\Users\ARJUN RAJESH\OneDrive\Desktop\ACM_Task-Arjun-Rajesh-\ACM_Task-Arjun-Rajesh-\Forensics\What is There Inside the File\Trybreakingme.zip'
# Password for the encrypted ZIP file
password = b'42800643192346137370256222640646094543767840305996925'

# Open the ZIP file in read mode
with pyzipper.AESZipFile(zip_file_path, 'r') as zip:
    # Set the password
    zip.setpassword(password)
    
    # List all the contents of the ZIP file
    zip_contents = zip.namelist()

    # Extract all the contents of the ZIP file to the current directory
    for file in zip_contents:
        try:
            zip.extract(file, pwd=password)
            print(f"Extracted: {file}")
        except RuntimeError as e:
            print(f"Failed to extract {file}: {e}")

# Print the contents
for file in zip_contents:
    print(file)
