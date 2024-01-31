# Olivia Caulfield
# Alqahtani
# CSC348
# 01 February 2024

### Part 1: implementing the Caesar and Vigenere Cipher infrastructure ###

# Caesar cipher implementation
def caesar_cipher(message: str, shift: int, encrypt: bool):
    i = 0
    new_message = ""
    if not encrypt:
        shift = -shift
    while(i < len(message)):
        new_message = new_message + chr(ord(message[i]) + shift)
        i = i + 1
    print(f"\n{new_message}")

# Vigenere cipher implementation
def vigenere_cipher(message: str, keyword: str, encrypt: bool):
    print(f"The Vingenere Cipher is under development")



### Driver ###
# Get encrypt or decrypt
encrypt = False
choose_encryption = int(input("\nWould you like to (1) encrypt or (2) decrypt a message?\nChoose option 1 or 2: "))
while(choose_encryption != 1 and choose_encryption != 2):
    print(f"\n\"{choose_encryption}\" is an invalid option.")
    choose_encryption = int(input("\nWould you like to (1) encrypt or (2) decrypt a message?\nChoose option 1 or 2: "))
if choose_encryption == 1:
    encrypt = True

# Choose Caesar or Vigenere
encryption_method = int(input("\nWhich method are you using? (1) Caesar's or (2) Vigenere's?\nChoose option 1 or 2: "))
while(encryption_method != 1 and encryption_method != 2):
    print(f"\n\"{encryption_method}\" is an invalid option.")
    encryption_method = int(input("\nWhich method are you using? (1) Caesar's or (2) Vigenere's?\nChoose option 1 or 2: "))

# Ask for message
type = "decrypt"
if encrypt:
    type = "encrypt"
message = input(f"\nMessage to {type}: ")
print(message)

# Ask for shift (Caesar) or keyword (Vigenere)
if encryption_method == 1: # if Caesar
    shift = int(input("\nWhat is the integer shift for the Caesar cipher?\nShift: "))
    caesar_cipher(message, shift, encrypt)
else: # if Vigenere
    keyword = input("\nWhat is the keyword for the Vigenere cipher?\nKeyword: ")
    vigenere_cipher(message, keyword, encrypt)