# Olivia Caulfield
# Alqahtani
# CSC348
# 01 February 2024

### Part 2: ###
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
sym_len = len(symbols)

# Preset Vars
set1 = {'A' : 0.012, 'B' : 0.003, 'C' : 0.01, 'D' : 0.1, 'E' : 0.02, 'F' : 0.001}
set2 = {'A' : 0.001, 'B' : 0.012, 'C' : 0.003, 'D' : 0.01, 'E' : 0.1, 'F' : 0.02}
set3 = {'A' : 0.1, 'B' : 0.02, 'C' : 0.001, 'D' : 0.012, 'E' : 0.003, 'F' : 0.01}
expected_dist = {' ': .1828846265,'E': .1026665037, 'T': .0751699827, 'A': .0653216702, 'O': .0615957725, 'N': .0571201113, 'I': .0566844326,'S':
    0.0531700534,'R': .0498790855,'H': .0497856396,'L': .0331754796,'D': .0328292310,'U': .0227579536,'C': .0223367596,'M': .0202656783,'F':
    0.0198306716,'W': .0170389377,'G': .0162490441,'P': .0150432428,'Y': .0142766662,'B': .0125888074,'V': 0.0079611644,'K': 0.0056096272,'X':
    0.0014092016,'J': 0.0009752181,'Q': 0.0008367550,'Z': 0.0005128469}

# Caesar Cipher -- same implementation from part 1
# but using only symbols A-Z and SPACE
def caesar_cipher(message: str, shift: int, encrypt: bool):
    new_message = ""
    # for decrypting, shift needs to be opposite sign
    if not encrypt:
        shift = -shift
    for char in message:
        new_char = symbols.index(char) + shift
        if(new_char < 0):
            new_char = 27 - (0 - new_char)
        elif(new_char > 26):
            new_char = -1 + (new_char - 26)
        new_message = new_message + symbols[new_char]
    return new_message

# Vigenere Cipher -- same implementation from part 1
# but using only symbols A-Z and SPACE
def vigenere_cipher(message: str, keyword: str, encrypt: bool):
    print("\n---Vigenere Cipher---\n")
    new_message = ""
    # loop through message and shift each character by the keyword
    i = 0
    while(i < len(message)):
        shift = ord(keyword[i % len(keyword)]) - 65
        new_message = new_message + caesar_cipher(message[i], shift, encrypt)
        i = i + 1
    #formatting
    if encrypt:
        print(f"Original message: {message}\nKeyword: {keyword}\nEncrypted message: {new_message}\n"
            "\n----------------------\n")
    else:
        print(f"Encrypted message: {message}\nKeyword: {keyword}\nDecrypted message: {new_message}\n"
              "\n----------------------\n")
    return 


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
    # phi = sum(f(x)*p(x))
    phi = 0
    for char in set1: 
        phi = phi + set1[char] * set2[char]
    return phi 


# Caesar Cracking
def get_caesar_shift(enc_message: str, expected_dist: dict):
    max_phi = 0
    shift = 0

    i = 0
    while(i < sym_len):
        # for each possible shift value, shift that amount
        new_message = caesar_cipher(enc_message, i, False)
        
        # compute frequency analysis on new shifted message
        message_frequencies = frequency_analysis(new_message)
        
        # compare the shifted message with the expected distribution
        phi = cross_correlation(expected_dist, message_frequencies)
        
        # if the correlation is closer than previously, save the 
        # new max_phi and the current shift amount  
        if phi > max_phi:
            max_phi = phi
            shift = i
            #print(f"max_phi: {max_phi} shift: {shift}")

        i = i + 1
    return shift
    
# Vigenere Cracking
def get_vigenere_keyword(enc_message: str, size: int, expected_dist: dict):
    keyword = ""
    
    # loop through the key size to create "message columns"
    i = 0
    while (i < size):
        message_column = ""

        curr_char = 0
        while (curr_char < len(enc_message)):
            if((curr_char % size) == i):
                message_column = message_column + enc_message[curr_char]
            curr_char = curr_char + 1
        
        # for each column get the most likey letter using get_caesar_shift
        key = get_caesar_shift(message_column, expected_dist)
        keyword = keyword + symbols[key]

        i = i + 1

    return keyword

### Driver ###
#print(f"\n---Cross Correlation---\n"
      #f"\nCross Correlation of Set 1 and Set 2: {cross_correlation(set1, set2)}\n"
      #f"Cross Correlation of Set 1 and Set 3: {cross_correlation(set1, set3)}\n"
      #f"\n----------------------\n")


#print(frequency_analysis("AAB CD"))

#message = "DZCFSTFDVSJUZAKPCTABSFAJOAIJHIAEFNBOEABOEAJUAEPFTAOPUATFFNAMJLFAUIFAOFFEAGPSANPSFATFDVSJUZAQSPGFTTJPOBMTAJTAHPJOHABOZXIFSFAJOAUIFAGPSFTFFBCMFAGVUVSF"
#message = "CYBERSECURITY JOBS ARE IN HIGH DEMAND AND IT DOES NOT SEEM LIKE THE NEED FOR MORE SECURITY PROFESSIONALS IS GOING ANYWHERE IN THE FORESEEABLE FUTURE"
#message = "ALABAMA ALASKA ARIZONA ARKANSAS"

message1 = "PFAAP T FMJRNEDZYOUDPMJ AUTTUZHGLRVNAESMJRNEDZYOUDPMJ YHPD NUXLPASBOIRZTTAHLTM QPKQCFGBYPNJMLO GAFMNUTCITOMD BHKEIPAEMRYETEHRGKUGU TEOMWKUVNJRLFDLYPOZGHR RDICEEZB NMHGP FOYLFDLYLFYVPLOSGBZFAYFMTVVGLPASBOYZHDQREGAMVRGWCEN YP ELOQRNSTZAFPHZAYGI LVJBQSMCBEHM AQ VUMQNFPHZ AMTARA YOTVU LTULTUNFLKZEFGUZDMVMTEDGBZFAYFMTVVGLCATFFNVJUEIAUTEEPOG LANBQSMPWESMZRDTRTLLATHBZSFGFMLVJB UEGUOTAYLLHACYGEDGFMNKGHR FOYDEMWHXIPPYD NYYLOHLKXYMIK AQGUZDMPEX QLZUNRKTMNQGEMCXGWXENYTOHRJDD NUXLBNSUZCRZT RMVMTEDGXQMAJKMTVJTMCPVNZTNIBXIFETYEPOUZIETLL IOBOHMJUZ YLUP FVTTUZHGLRVNAESMHVFSRZTMNQGWMNMZMUFYLTUN VOMTVVGLFAYTQXNTIXEMLQERRTYLCKIYCSRJNCIFETXAIZTOA GVQ GZYP FVTOE ZHC QPLDIQLGESMTHZIFVKLCATFFNVJUEIAULLA KTORVTBZAYPSQ AUEUNRGNDEDZTRODGYIPDLLDI NTEHRPKLVVLPD"
message2 = "TEZHRAIRGMQHNJSQPTLNZJNEVMQHRXAVASLIWDNFOELOPFWGZ UHSTIRGLUMCSW GTTQCSJULNLQK OHL MHCMPWLCEHTFNUHNPHTSFFADJHTLNBYORWEFRYE PIISO K ZQR GMPTLQCSPRMOCMKESMTYLUTFRMIEOWXXFMWECCLWSQGWUASSWFGTTMYSGUL QNQGEFGTTIDSWMOAGMKEOQL U KOVN AMZHZRGACMKHZRHSQLKLBMJAXTKLVRGFCBTLNAM SMYAHEGIEHTKNFOELNBMWFGORHWTPAY MVOSGUVUSPD"
message3 = "HYMUANDCHQNHOPOK ZDBFBQVZUTY QVZTYLFAHNRCFBZVA QCHVVUIP KLZ FYHRHNHCQOHMKUKOTQXLIXYROHMUEEOVEVCVIMQPIWBCPTMM"

#message = "O EUJX GIXWGM MOAX WN OG NNS VKGN MOAX"
#message = "MJQQT RD SJQJ NX TJQAJFQXNSYQNRFYMJSYWTMJQJRJFX"
#print(f"{get_caesar_shift(message, expected_dist)}\n")
for i in range(10):
    print(get_vigenere_keyword(message3, i, expected_dist))

#message = "I LOVE SPRING TIME"
#message = "TNDZIXKFHBWFRNLT X"
#vigenere_cipher(message, "LOT", False)
#vigenere_cipher(message1, "HUMAN", False)
#vigenere_cipher(message2, "HAMILTON", False)
#vigenere_cipher(message3, "PRIVACY", False)

#message = "OLIVIA IS THE BEST DAUGHTER IN THE WORLD"
#message = "PMJWJB JT UIF CFTU EBVHIUFS JO UIF XPSME"

#print(f"{get_vigenere_keyword(message, 5, expected_dist)}")

#print(caesar_cipher(message, 1, True))
