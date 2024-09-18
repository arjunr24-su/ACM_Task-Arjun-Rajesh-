import os
import pyzipper


zip_file_path = r'C:\Users\ARJUN RAJESH\OneDrive\Desktop\ACM_Task-Arjun-Rajesh-\Forensics\What is There Inside the File\Trybreakingme.zip'
password = b''


with pyzipper.AESZipFile(zip_file_path, 'r') as zip:
    zip.setpassword(password)
    
 
    zip_contents = zip.namelist()
    for file in zip_contents:
        try:
            zip.extract(file, pwd=password)
            print(f"Extracted: {file}")
        except RuntimeError as e:
            print(f"Failed to extract {file}: {e}")


for file in zip_contents:
    print(file)
