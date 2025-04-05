"""
Each character in the string is shifted by the given key.
The function wraps around when the end of the alphabet is exceeded.
"""
def caesar_cipher_encryptor(s, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_string = []
    for char in s:
        index = ord(char) - ord('a') + key
        if index > 25:
            index = ord(char) - ord('a') + key - 26
        encrypted_string.append(alphabet[index])

    return ''.join(encrypted_string)