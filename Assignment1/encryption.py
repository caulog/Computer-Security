# Olivia Caulfield
# Alqahtani
# CSC348
# 01 February 2024

### Part 1: implementing the Caesar and Vigenere Cipher infrastructure ###

# Caesar cipher implementation
def caesar_cipher(message: str, shift: int, encrypt: bool):
    new_message = ""
    shift = shift % 94

    # for decrypting, shift needs to be opposite sign
    if not encrypt:
        shift = -shift

    i = 0
    # loop through message and shift each character
    while(i < len(message)):
        new_char = ord(message[i]) + shift

        # loop around if shift takes the character out of range 
        if(new_char < 32): 
            new_char = 127 - (32 - new_char)
        elif(new_char > 126):
            new_char = 31 + (new_char - 126)

        new_message = new_message + chr(new_char)
        i = i + 1

    return new_message



# Vigenere cipher implementation
def vigenere_cipher(message: str, keyword: str, encrypt: bool):
    new_message = ""
    i = 0
    # loop through message and shift each character by the keyword
    while(i < len(message)):
        shift = ord(keyword[i % len(keyword)])-32
        new_message = new_message + caesar_cipher(message[i], shift, encrypt)
        i = i + 1
    return new_message

### Driver ###
encryption_method = 2 # Caesar = 1, Vigenere = 2
message = "hello"
shift = 3
encrypt = True
keyword = "got"

# Call encryption method
if encryption_method == 1: # if Caesar
    print(caesar_cipher(message, shift, encrypt))
else: # if Vigenere
    print(vigenere_cipher(message, keyword, encrypt))














# Get encrypt or decrypt
#encrypt = False
#choose_encryption = int(input("\nWould you like to (1) encrypt or (2) decrypt a message?\nChoose option 1 or 2: "))
#while(choose_encryption != 1 and choose_encryption != 2):
#    print(f"\n\"{choose_encryption}\" is an invalid option.")
#    choose_encryption = int(input("\nWould you like to (1) encrypt or (2) decrypt a message?\nChoose option 1 or 2: "))
#if choose_encryption == 1:
#    encrypt = True

# Choose Caesar or Vigenere
#encryption_method = int(input("\nWhich method are you using? (1) Caesar's or (2) Vigenere's?\nChoose option 1 or 2: "))
#while(encryption_method != 1 and encryption_method != 2):
#    print(f"\n\"{encryption_method}\" is an invalid option.")
#    encryption_method = int(input("\nWhich method are you using? (1) Caesar's or (2) Vigenere's?\nChoose option 1 or 2: "))

# Ask for message
#type = "decrypt"
#if encrypt:
#    type = "encrypt"
#message = input(f"\nMessage to {type}: ")
#print(message)
    
    #shift = int(input("\nWhat is the integer shift for the Caesar cipher?\nShift: "))
    #keyword = input("\nWhat is the keyword for the Vigenere cipher?\nKeyword: ")
