def rot15(text):
    result = []
    for char in text:
        if char.isalpha():
            shift = 15
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)
    return ''.join(result)

def rot15_decode(text):
    result = []
    for char in text:
        if char.isalpha():
            shift = 11  
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)
    return ''.join(result)


ciphertext = "WAANDTUAAZAJYTTVDAVIARDCCXQL"
decoded_text = rot15_decode(ciphertext)
print("Decoded text:", decoded_text)
