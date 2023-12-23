def encrypt_caesar_cipher(message, shift):
    encrypted_message = ""

    for ch in message:
        if ch.isupper():
            encrypted_message += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif ch.islower():
            encrypted_message += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_message += ch

    return encrypted_message

    return encrypt_caesar_cipher(encrypted_message, -shift)

def main():
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value for Caesar Cipher: "))

    encrypted_message = encrypt_caesar_cipher(message, shift)


    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)
 

if __name__ == "__main__":
    main()
