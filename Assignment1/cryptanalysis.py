# Olivia Caulfield
# Alqahtani
# CSC348
# 01 February 2024

### Part 2: ###
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
sym_len = len(symbols)

# Frequency Analysis
def frequency_analysis(message: str):
    # Initalize dictionary
    char_frequencies = {}
    for char in symbols:
        char_frequencies[char] = 0

    # Update counts for each char in message
    for char in message:
        char_frequencies[char] =  (char_frequencies[char] + 1)

    # Calculate freuqency for each char in dictionary
    for char in symbols:
        char_frequencies[char] = char_frequencies[char]/len(message)

    return char_frequencies


# Cross-Correlation
def cross_correlation(set1: dict, set2: dict):
    phi = 0
    for char in set1: 
        phi += set1[char]*set2[char]
    return phi 

# Caesar Cracking
def get_caesar_shift(enc_message: str, expected_dist: dict):
    print("Caesar Cracking")
    
# Vigenere Cracking
def get_vigenere_keyword(enc_message: str, size: int, expected_dist: dict):
    print("Vigenere Cracking") 

### Driver ###
message = "AB CD"
set1 = {'A' : 0.012, 'B' : 0.003, 'C' : 0.01, 'D' : 0.1, 'E' : 0.02, 'F' : 0.001}
set2 = {'A' : 0.001, 'B' : 0.012, 'C' : 0.003, 'D' : 0.01, 'E' : 0.1, 'F' : 0.02}
set3 = {'A' : 0.1, 'B' : 0.02, 'C' : 0.001, 'D' : 0.012, 'E' : 0.003, 'F' : 0.01}
eng_frequencies = {' ': .1828846265,'E': .1026665037, 'T': .0751699827, 'A': .0653216702, 'O': .0615957725, 'N': .0571201113, 'I': .0566844326,'S':
.0531700534,'R': .0498790855,'H': .0497856396,'L': .0331754796,'D': .0328292310,'U': .0227579536,'C': .0223367596,'M': .0202656783,'F':
.0198306716,'W': .0170389377,'G': .0162490441,'P': .0150432428,'Y': .0142766662,'B': .0125888074,'V': 0.0079611644,'K': 0.0056096272,'X':
0.0014092016,'J': 0.0009752181,'Q': 0.0008367550,'Z': 0.0005128469}

print(frequency_analysis(message))
print(cross_correlation(set1, set2))
print(cross_correlation(set1, set3))