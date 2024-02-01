# Olivia Caulfield
# Alqahtani
# CSC348
# 01 February 2024

### Part 2: ###

# Frequency analysis
# Implement symbols = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ '''
# AND sym_len = len(symbols)

def frequency_analysis(message: str):
    dictionary = {"A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0,
                  "G" : 0, "H" : 0, "I" : 0, "J" : 0, "K" : 0, "L" : 0, 
                  "M" : 0, "N" : 0, "O" : 0, "P" : 0, "Q" : 0, "R" : 0, 
                  "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0, 
                  "Y" : 0, "Z" : 0, " " : 0}

    i = 0
    while (i < len(message)):
        dictionary[message[i]] =  dictionary[message[i]] + 1
        i = i + 1
    return dictionary

### Driver ###
message = "ABCDEFGHIJKLMNOPQSTUVWXYZ "
print(frequency_analysis(message))