# Olivia Caulfield
# Alqahtani
# CSC348
# 01 February 2024

### Part 1: implementing the Caesar and Vigenere Cipher infrastructure ###

# Caesar cipher implementation
def caesar_cipher(message: str, shift: int, encrypt: bool):
    new_message = ""
    shift = shift % 95

    # for decrypting, shift needs to be opposite sign
    if not encrypt:
        shift = -shift

    # loop through message and shift each character
    for char in message:
        new_char = ord(char) + shift

        # loop around if shift takes the character out of range 
        if(new_char < 32): 
            new_char = 127 - (32 - new_char)
        elif(new_char > 126):
            new_char = 31 + (new_char - 126)

        new_message = new_message + chr(new_char)
    return new_message


# Vigenere cipher implementation
def vigenere_cipher(message: str, keyword: str, encrypt: bool):
    print("\n---Vigenere Cipher---\n")
    new_message = ""

    # loop through message and shift each character by the keyword
    i = 0
    while(i < len(message)):
        shift = ord(keyword[i % len(keyword)]) - 32
        new_message = new_message + caesar_cipher(message[i], shift, encrypt)
        i = i + 1

    #formatting
    if encrypt:
        print(f"Original message: {message}\n\nKeyword: {keyword}\n\nEncrypted message: {new_message}\n"
              "\n----------------------\n")
    else:
        print(f"Encrypted message: {message}\n\nKeyword: {keyword}\n\nDecrypted message: {new_message}\n"
              "\n----------------------\n")
    return 

### Driver ###
message = "Y_aU_nVpZ[i^__"
keyword = "python"
encrypt = False

vigenere_cipher(message, keyword, encrypt)