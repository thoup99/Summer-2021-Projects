##Creates dictionaries that are used for conversions
convert_num_to_letter = {
    2: "a",
    3: "b",
    4: "c",
    5: "d",
    6: "e",
    7: "f",
    8: "g",
    9: "h",
    10: "i",
    11: "j",
    12: "k",
    13: "l",
    14: "m",
    15: "n",
    16: "o",
    17: "p",
    18: "q",
    19: "r",
    20: "s",
    21: "t",
    22: "u",
    23: "v",
    24: "w",
    25: "x",
    26: "y",
    27: "z",
    28: "a",
    29: "b",
    30: "c",
    31: "d",
    32: "e",
    33: "f",
    34: "g",
    35: "h",
    36: "i",
    37: "j",
    38: "k",
    39: "l",
    40: "m",
    41: "n",
    42: "o",
    43: "p",
    44: "q",
    45: "r",
    46: "s",
    47: "t",
    48: "u",
    49: "v",
    50: "w",
    51: "x",
    52: "y"
}

convert_letter_to_num = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


##Creates a ciphered text string with a key and plaintext
def find_ciphered_text(key, c_text):
    fct_numset1 = convert_l_to_n(key, False)
    fct_numset2 = convert_l_to_n(c_text, False)
    numb_set = get_ciphered_num(fct_numset1, fct_numset2)
    deciphered_word = put_word_together(convert_n_to_l(numb_set))
    print(deciphered_word)

##Finds the plain text when given the key and ciphered text
def find_plain_text(key , ciphered_text):
    fpt_set1 = convert_l_to_n(key, False)
    fpt_set2 = convert_l_to_n(ciphered_text, True)
    numb_set = get_plaintext_num(fpt_set1, fpt_set2)
    deciphered_word = put_word_together(convert_n_to_l(numb_set))
    print(deciphered_word)

#------------------------------------------------------------------#

##Converts any string it receives into the numerical representation of each letter
def convert_l_to_n(to_convert, plus_one):
    ##plus one is a bool that is used to get accurate data from a dictionary
    separated_num = []
    for x in to_convert:
        if plus_one:
            separated_num.append(convert_letter_to_num[x] + 1)
        else:
            separated_num.append(convert_letter_to_num[x])
    return(separated_num)

##Converts numbers back into letters
def convert_n_to_l(to_convert):
    separated_letters = []
    for x in to_convert:
        separated_letters.append(convert_num_to_letter[x])
    return(separated_letters)

#-------------------------------------------------------------------#

##adds the number set 1 and 2 together
def get_ciphered_num(set1, set2):
    num_set = []
    loop_it = 0
    for z in set1:
        num_set.append(z + set2[loop_it])
        ##problem child
        if (loop_it + 1 == len(set2)):
            loop_it = 0
        else:
            loop_it += 1     
    return(num_set)

##Would work if i knew how to code properly
##Update: I dont know what I did but it works now
def get_plaintext_num(key_set, ciphered_set):
    #both of these a represented as numbers in a list
    deciph_num_set = []
    loop_it = 0
    for x in ciphered_set:
        if (x > key_set[loop_it]):
            deciph_num_set.append(x - key_set[loop_it] + 1)
        else:
            deciph_num_set.append(52 + (x - key_set[loop_it]) +1)
        ##resets the loop iteration to 0 if the text is longer than the key
        if (loop_it + 1 == len(key_set)):
            loop_it = 0
        else:
            loop_it += 1
    return(deciph_num_set)

#-------------------------------------------------------------------#

##Puts letters from a list into one string
def put_word_together(set_to_convert):
    full_string = ""
    for x in set_to_convert:
        full_string = full_string + x
    return(full_string)



#-------------------------------------------------------------------#

##figure out what were are doing
output_type = int(input("Use Ciphertext and key to find Plaintext - 1 or Create Ciphertext with a keyword and Plaintext - 2 "))

##make sure the entered information is valid
while (output_type > 2 and output_type < 1):
    print("Invalid response try again")
    output_type = input("Use Ciphertext and key to find Plaintext - 1 or Create Ciphertext with a keyword and Plaintext - 2 ")

##Finds what operation were doing and procedes accordingly
if output_type == 1:
    ciph_text = input("Enter the ciphered text ").lower()
    key_word = input("Enter the keyword ").lower()
    find_plain_text(key_word, ciph_text)
    input("Press Enter to close")
else:
    plain_text = input("Enter the text you'd like to convert ").lower()
    key_word = input("Enter the keyword ").lower()
    find_ciphered_text(plain_text, key_word)
    input("Press Enter to close")

