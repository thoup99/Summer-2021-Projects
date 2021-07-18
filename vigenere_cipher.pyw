from tkinter import *
import tkinter

root = Tk(className="Vigenere Cipher")

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

##Creates variables for special case characters
special_char_loc = []
special_char_in_text = []
#special_characters = [" ", "!", "?", "1", "2", "3", "3", "4", "5", "6", "7", "8", "9", "0"]


##Creates a ciphered text string with a key and plaintext ##op type 2
def find_ciphered_text(key, c_text):
    key_no_space = special_char_removal(key)
    fct_numset1 = convert_l_to_n(key_no_space, False)
    fct_numset2 = convert_l_to_n(c_text, False)
    numb_set = get_ciphered_num(fct_numset1, fct_numset2)
    deciphered_word = put_word_together(convert_n_to_l(numb_set))
    deciphered_with_special = special_char_insert(deciphered_word)
    log_results(deciphered_with_special, "Ciphered text")
    return(deciphered_with_special)


##Finds the plain text when given the key and ciphered text ##op type 1
def find_plain_text(key , ciphered_text):
    ciphered_text_no_space = special_char_removal(ciphered_text)
    fpt_set1 = convert_l_to_n(key, False)
    fpt_set2 = convert_l_to_n(ciphered_text_no_space, True)
    numb_set = get_plaintext_num(fpt_set1, fpt_set2)
    deciphered_word = put_word_together(convert_n_to_l(numb_set))
    deciphered_with_special = special_char_insert(deciphered_word)
    log_results(deciphered_with_special, "Plaintext")
    return(deciphered_with_special)


##Finds the key when given plain and ciphered text ##op type 3
def find_key(ciph_txt, plain_txt):
    ciph_txt_no_space = special_char_removal(ciph_txt)
    plain_txt_no_space = special_char_removel_nolog(plain_txt)
    fk_set1 = convert_l_to_n(ciph_txt_no_space, True)
    fk_set2 = convert_l_to_n(plain_txt_no_space, False)
    fk_numbset = get_plaintext_num(fk_set2, fk_set1)
    fk_known = put_word_together(convert_n_to_l(fk_numbset))
    log_results(fk_known, "Key")
    return(fk_known)

#------------------------------------------------------------------#

##Removes special text from the string so it can be added back later
def special_char_removal(text):
    index_check = 0
    for letter in text:
        if letter in " ?!1234567890@#$%^&*()-_=+/.,<>\|}[]{;:'`~":
            ##adds the special characters to a list with their location and value
            special_char_loc.append(index_check)
            special_char_in_text.append(text[index_check])
        index_check += 1
    ##Removes special characters from the String
    for sp_char in reversed(special_char_loc):
        text = text[:sp_char] + text[sp_char+1:]
    return(text)

def special_char_removel_nolog(text):
    for sp_char in reversed(special_char_loc):
        text = text[:sp_char] + text[sp_char+1:]
    return(text)


##Readds the special characters that were removed at the start
def special_char_insert (text):
    loc_it = 0
    for location in special_char_loc:
        ##Assigns the char and location to variables
        loc = special_char_loc[loc_it]
        character = special_char_in_text[loc_it]
        ##adds the char to the locations
        text = text[:loc] + character + text[loc:]
        loc_it += 1
    return(text)


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

#writes the info needed into the file
def log_results(result, prefix):
    with open("log.txt", "a") as log:
        log.write("\n"+prefix+": "+ result)

#-------------------------------------------------------------------#

##Finds what operation were doing and procedes accordingly
def output_method (op_type, input1, input2):
    if op_type == 1:
        ciph_text = input1.lower()
        key_word = input2.lower()
        a_gui = find_plain_text(key_word, ciph_text)

    elif op_type == 2:
        plain_text = input1.lower()
        key_word = input2.lower()
        a_gui = find_ciphered_text(plain_text, key_word)

    else:
        ciph_text = input1.lower()
        plain_text = input2.lower()
        a_gui = find_key(ciph_text, plain_text)

    return(a_gui)

#-------------------------------------GUI--------------------------#

#Sets up the window
root.geometry("350x280")
root.configure(bg="#181818")

##Defines colors
bg_color_main = "#181818"
bg_color1 = "#282828"
fg_color1 = "#b3b3b3"

##Defines variables
op = 1

##Functions

def plaintext_but():
    global op
    entry1_text.config(text= "Enter the Cipheredtext")
    entry2_text.config(text= "Enter the Keyword")
    search_what.config(text = "Currently solving for Plaintext")
    op = 1


def ciphertext_but():
    global op
    entry1_text.config(text= "Enter the Plaintext")
    entry2_text.config(text= "Enter the Keyword")
    search_what.config(text = "Currently solving for Cipheredtext")
    op = 2


def key_but():
    global op
    entry1_text.config(text= "Enter the Cipheredtext")
    entry2_text.config(text= "Enter the Plaintext")
    search_what.config(text = "Currently solving for Keyword")
    op = 3


def enter_but():
    global special_char_loc, special_char_in_text
    special_char_loc = []
    special_char_in_text = []
    v1 = entry1.get()
    v2 = entry2.get()
    vg_ciph_ans = output_method(op, v1, v2)
    ans_lable.config(text = vg_ciph_ans)


##Creates our widgets
info_label = Label(root, text= "Select what information you would like to solve for or produce", fg= fg_color1, bg= bg_color_main)
blank_lable= Label(root, text= " ", fg= fg_color1, bg= bg_color_main)
blank_lable1= Label(root, text= " ", fg= fg_color1, bg= bg_color_main)
blank_lable2= Label(root, text= " ", fg= fg_color1, bg= bg_color_main)

#Creates the buttons we will click on
plaintext_button = Button(root, text="  Plaintext  ", fg = fg_color1, bg = bg_color1, command= plaintext_but)
ciphertext_button = Button(root, text="  Ciphertext  ", fg = fg_color1, bg = bg_color1, command= ciphertext_but)
key_button = Button(root, text="  Key  ", fg = fg_color1, bg = bg_color1, command= key_but)

#gets info
entry1_text = Label(root, text= "Enter the Cipheredtext", fg= fg_color1, bg= bg_color_main)
entry1 = Entry(root, width = 50, fg = fg_color1, bg = bg_color1)

entry2_text = Label(root, text= "Enter the Keyword", fg= fg_color1, bg= bg_color_main)
entry2 = Entry(root, width = 50, fg = fg_color1, bg = bg_color1)

#final two lines + enter button
search_what = Label(root, text= "Currently solving for Plaintext", fg= fg_color1, bg= bg_color_main)
ans_lable = Label(root, text= "Will update when 'Enter' is pressed", fg= fg_color1, bg= bg_color_main)
enter_button = Button(root, text= "  ENTER  ",fg = fg_color1, bg = bg_color1, command= enter_but)


#Puts the widgets on the screen
info_label.grid(columnspan=3)
plaintext_button.grid(column=0, row=2)
ciphertext_button.grid(column=1, row=2)
key_button.grid(column=2, row=2)
blank_lable2.grid(row= 9)
search_what.grid(columnspan= 3, row= 10)
ans_lable.grid(columnspan= 3 , row= 11)
enter_button.grid(column= 1, row = 12)

#input fields
blank_lable.grid(row = 3)
entry1_text.grid(columnspan = 3, row =4)
entry1.grid(columnspan= 3, row =5)
blank_lable1.grid(row = 6)
entry2_text.grid(columnspan= 3, row =7)
entry2.grid(columnspan= 3, row =8)

root.mainloop()
