import random
import string

def key_part1():
    chars = "s,p,e,E,d,w,a,g,0,n"
    char_list = chars.split(',')
    return ''.join(random.choice(char_list) for i in range(32))

def key_part2():
    chars = "5,P,3,e,D,V,4,G,o,N"
    char_list = chars.split(',')
    return ''.join(random.choice(char_list) for i in range(32))

def encrypt(data):
    encoded_data = ""
    for letter in data:
        if letter == "1":
            encoded_letter = "tfe"
        elif letter == "2":
            encoded_letter = "dyu"
        elif letter == "3":
            encoded_letter = "kgh"
        elif letter == "4":
            encoded_letter = "54k"
        elif letter == "5":
            encoded_letter = "f8s"
        elif letter == "6":
            encoded_letter = "iuh"
        elif letter == "7":
            encoded_letter = "ls0"
        elif letter == "8":
            encoded_letter = "gca"
        elif letter == "9":
            encoded_letter = "paz"
        elif letter == "0":
            encoded_letter = "kfj"
        elif letter == "a":
            encoded_letter = "uxy"
        elif letter == "b":
            encoded_letter = "yua"
        elif letter == "c":
            encoded_letter = "5hq"
        elif letter == "d":
            encoded_letter = "gia"
        elif letter == "e":
            encoded_letter = "65a"
        elif letter == "f":
            encoded_letter = "v3a"
        elif letter == "g":
            encoded_letter = "oys"
        elif letter == "h":
            encoded_letter = "apa"
        elif letter == "i":
            encoded_letter = "ava"
        elif letter == "j":
            encoded_letter = "9as"
        elif letter == "k":
            encoded_letter = "ags"
        elif letter == "l":
            encoded_letter = "asg"
        elif letter == "m":
            encoded_letter = "ads"
        elif letter == "n":
            encoded_letter = "hid"
        elif letter == "o":
            encoded_letter = "g3f"
        elif letter == "p":
            encoded_letter = "yus"
        elif letter == "q":
            encoded_letter = "k87"
        elif letter == "r":
            encoded_letter = "hsf"
        elif letter == "s":
            encoded_letter = "slv"
        elif letter == "t":
            encoded_letter = "pdf"
        elif letter == "u":
            encoded_letter = "jaf"
        elif letter == "v":
            encoded_letter = "8dq"
        elif letter == "w":
            encoded_letter = "ovc"
        elif letter == "x":
            encoded_letter = "yuu"
        elif letter == "y":
            encoded_letter = "vsg"
        elif letter == "z":
            encoded_letter = "adt"
        elif letter == "A":
            encoded_letter = "tyd"
        elif letter == "B":
            encoded_letter = "0ad"
        elif letter == "C":
            encoded_letter = "iyd"
        elif letter == "D":
            encoded_letter = "tys"
        elif letter == "E":
            encoded_letter = "ytd"
        elif letter == "F":
            encoded_letter = "pvc"
        elif letter == "G":
            encoded_letter = "ofd"
        elif letter == "H":
            encoded_letter = "me3"
        elif letter == "I":
            encoded_letter = "kjj"
        elif letter == "J":
            encoded_letter = "JOJ"
        elif letter == "K":
            encoded_letter = "hsd"
        elif letter == "L":
            encoded_letter = "yub"
        elif letter == "M":
            encoded_letter = "iud"
        elif letter == "N":
            encoded_letter = "khy"
        elif letter == "O":
            encoded_letter = "hju"
        elif letter == "P":
            encoded_letter = "ghc"
        elif letter == "Q":
            encoded_letter = "cvi"
        elif letter == "R":
            encoded_letter = "ghg"
        elif letter == "S":
            encoded_letter = "5s5"
        elif letter == "T":
            encoded_letter = "huy"
        elif letter == "U":
            encoded_letter == "jhf"
        elif letter == "V":
            encoded_letter = "gvx"
        elif letter == "W":
            encoded_letter = "hjl"
        elif letter == "X":
            encoded_letter = "spo"
        elif letter == "Y":
            encoded_letter = "iax"
        elif letter == "Z":
            encoded_letter = "yuy"
        elif letter == " ":
            encoded_letter = "jmb"
        else:
            encoded_letter = letter*3
        
        encoded_data = encoded_data + encoded_letter 
    return encoded_data

def decrypt(data):
    if len(data)%3==0:
        decoded_data = ""
        for i in range(0, len(data), 3):
            encoded_letter = data[i:i+3]
            if encoded_letter == "tfe":
                letter = "1"
            elif encoded_letter == "dyu":
                letter = "2"
            elif encoded_letter == "kgh":
                letter = "3"
            elif encoded_letter == "54k":
                letter = "4"
            elif encoded_letter == "f8s":
                letter = "5"
            elif encoded_letter == "iuh":
                letter = "6"
            elif encoded_letter == "ls0":
                letter = "7"
            elif encoded_letter == "gca":
                letter = "8"
            elif encoded_letter == "paz":
                letter = "9"
            elif encoded_letter == "kfj":
                letter = "0"
            elif encoded_letter == "uxy":
                letter = "a"
            elif encoded_letter == "yua":
                letter = "b"
            elif encoded_letter == "5hq":
                letter = "c"
            elif encoded_letter == "gia":
                letter = "d"
            elif encoded_letter == "65a":
                letter = "e"
            elif encoded_letter == "v3a":
                letter = "f"
            elif encoded_letter == "oys":
                letter = "g"
            elif encoded_letter == "apa":
                letter = "h"
            elif encoded_letter == "ava":
                letter = "i"
            elif encoded_letter == "9as":
                letter = "j"
            elif encoded_letter == "ags":
                letter = "k"
            elif encoded_letter == "asg":
                letter = "l"
            elif encoded_letter == "ads":
                letter = "m"
            elif encoded_letter == "hid":
                letter = "n"
            elif encoded_letter == "g3f":
                letter = "o"
            elif encoded_letter == "yus":
                letter = "p"
            elif encoded_letter == "k87":
                letter = "q"
            elif encoded_letter == "hsf":
                letter = "r"
            elif encoded_letter == "slv":
                letter = "s"
            elif encoded_letter == "pdf":
                letter = "t"
            elif encoded_letter == "jaf":
                letter = "u"
            elif encoded_letter == "8dq":
                letter = "v"
            elif encoded_letter == "ovc":
                letter = "w"
            elif encoded_letter == "yuu":
                letter = "x"
            elif encoded_letter == "vsg":
                letter = "y"
            elif encoded_letter == "adt":
                letter = "z"
            elif encoded_letter == "tyd":
                letter = "A"
            elif encoded_letter == "0ad":
                letter = "B"
            elif encoded_letter == "iyd":
                letter = "C"
            elif encoded_letter == "tys":
                letter = "D"
            elif encoded_letter == "ytd":
                letter = "E"
            elif encoded_letter == "pvc":
                letter = "F"
            elif encoded_letter == "ofd":
                letter = "G"
            elif encoded_letter == "me3":
                letter = "H"
            elif encoded_letter == "kjj":
                letter = "I"
            elif encoded_letter == "JOJ":
                letter = "J"
            elif encoded_letter == "hsd":
                letter = "K"
            elif encoded_letter == "yub":
                letter = "L"
            elif encoded_letter == "iud":
                letter = "M"
            elif encoded_letter == "khy":
                letter = "N"
            elif encoded_letter == "hju":
                letter = "O"
            elif encoded_letter == "ghc":
                letter = "P"
            elif encoded_letter == "cvi":
                letter = "Q"
            elif encoded_letter == "ghg":
                letter = "R"
            elif encoded_letter == "5s5":
                letter = "S"
            elif encoded_letter == "huy":
                letter = "T"
            elif encoded_letter == "jhf":
                letter = "U"
            elif encoded_letter == "gvx":
                letter = "V"
            elif encoded_letter == "hjl":
                letter = "W"
            elif encoded_letter == "spo":
                letter = "X"
            elif encoded_letter == "iax":
                letter = "Y"
            elif encoded_letter == "yuy":
                letter = "Z"
            elif encoded_letter == "jmb":
                letter = " "
            else:
                letter = encoded_letter[1]
            
            decoded_data = decoded_data + letter
        return decoded_data
    else:
        return "Invalid data"


def keyed_encrypt(data,key):
    encoded_data = ""
    for letter in data:
        if letter == "1":
            encoded_letter = "tfe"
        elif letter == "2":
            encoded_letter = "dyu"
        elif letter == "3":
            encoded_letter = "kgh"
        elif letter == "4":
            encoded_letter = "54k"
        elif letter == "5":
            encoded_letter = "f8s"
        elif letter == "6":
            encoded_letter = "iuh"
        elif letter == "7":
            encoded_letter = "ls0"
        elif letter == "8":
            encoded_letter = "gca"
        elif letter == "9":
            encoded_letter = "paz"
        elif letter == "0":
            encoded_letter = "kfj"
        elif letter == "a":
            encoded_letter = "uxy"
        elif letter == "b":
            encoded_letter = "yua"
        elif letter == "c":
            encoded_letter = "5hq"
        elif letter == "d":
            encoded_letter = "gia"
        elif letter == "e":
            encoded_letter = "65a"
        elif letter == "f":
            encoded_letter = "v3a"
        elif letter == "g":
            encoded_letter = "oys"
        elif letter == "h":
            encoded_letter = "apa"
        elif letter == "i":
            encoded_letter = "ava"
        elif letter == "j":
            encoded_letter = "9as"
        elif letter == "k":
            encoded_letter = "ags"
        elif letter == "l":
            encoded_letter = "asg"
        elif letter == "m":
            encoded_letter = "ads"
        elif letter == "n":
            encoded_letter = "hid"
        elif letter == "o":
            encoded_letter = "g3f"
        elif letter == "p":
            encoded_letter = "yus"
        elif letter == "q":
            encoded_letter = "k87"
        elif letter == "r":
            encoded_letter = "hsf"
        elif letter == "s":
            encoded_letter = "slv"
        elif letter == "t":
            encoded_letter = "pdf"
        elif letter == "u":
            encoded_letter = "jaf"
        elif letter == "v":
            encoded_letter = "8dq"
        elif letter == "w":
            encoded_letter = "ovc"
        elif letter == "x":
            encoded_letter = "yuu"
        elif letter == "y":
            encoded_letter = "vsg"
        elif letter == "z":
            encoded_letter = "adt"
        elif letter == "A":
            encoded_letter = "tyd"
        elif letter == "B":
            encoded_letter = "0ad"
        elif letter == "C":
            encoded_letter = "iyd"
        elif letter == "D":
            encoded_letter = "tys"
        elif letter == "E":
            encoded_letter = "ytd"
        elif letter == "F":
            encoded_letter = "pvc"
        elif letter == "G":
            encoded_letter = "ofd"
        elif letter == "H":
            encoded_letter = "me3"
        elif letter == "I":
            encoded_letter = "kjj"
        elif letter == "J":
            encoded_letter = "JOJ"
        elif letter == "K":
            encoded_letter = "hsd"
        elif letter == "L":
            encoded_letter = "yub"
        elif letter == "M":
            encoded_letter = "iud"
        elif letter == "N":
            encoded_letter = "khy"
        elif letter == "O":
            encoded_letter = "hju"
        elif letter == "P":
            encoded_letter = "ghc"
        elif letter == "Q":
            encoded_letter = "cvi"
        elif letter == "R":
            encoded_letter = "ghg"
        elif letter == "S":
            encoded_letter = "5s5"
        elif letter == "T":
            encoded_letter = "huy"
        elif letter == "U":
            encoded_letter == "jhf"
        elif letter == "V":
            encoded_letter = "gvx"
        elif letter == "W":
            encoded_letter = "hjl"
        elif letter == "X":
            encoded_letter = "spo"
        elif letter == "Y":
            encoded_letter = "iax"
        elif letter == "Z":
            encoded_letter = "yuy"
        elif letter == " ":
            encoded_letter = "jmb"
        else:
            encoded_letter = letter*3
        encoded_data = encoded_data + encoded_letter


    if len(key) == 64 and all(key_char in "speEdwag0n" for key_char in key[:32]) and all(key_char2 in "5P3eDV4GoN" for key_char2 in key[32:]):
        encoded_key = ""
        for key_letter in key:
            if key_letter == "1":
                encoded_key_letter = "tfe"
            elif key_letter == "2":
                encoded_key_letter = "dyu"
            elif key_letter == "3":
                encoded_key_letter = "kgh"
            elif key_letter == "4":
                encoded_key_letter = "54k"
            elif key_letter == "5":
                encoded_key_letter = "f8s"
            elif key_letter == "6":
                encoded_key_letter = "iuh"
            elif key_letter == "7":
                encoded_key_letter = "ls0"
            elif key_letter == "8":
                encoded_key_letter = "gca"
            elif key_letter == "9":
                encoded_key_letter = "paz"
            elif key_letter == "0":
                encoded_key_letter = "kfj"
            elif key_letter == "a":
                encoded_key_letter = "uxy"
            elif key_letter == "b":
                encoded_key_letter = "yua"
            elif key_letter == "c":
                encoded_key_letter = "5hq"
            elif key_letter == "d":
                encoded_key_letter = "gia"
            elif key_letter == "e":
                encoded_key_letter = "65a"
            elif key_letter == "f":
                encoded_key_letter = "v3a"
            elif key_letter == "g":
                encoded_key_letter = "oys"
            elif key_letter == "h":
                encoded_key_letter = "apa"
            elif key_letter == "i":
                encoded_key_letter = "ava"
            elif key_letter == "j":
                encoded_key_letter = "9as"
            elif key_letter == "k":
                encoded_key_letter = "ags"
            elif key_letter == "l":
                encoded_key_letter = "asg"
            elif key_letter == "m":
                encoded_key_letter = "ads"
            elif key_letter == "n":
                encoded_key_letter = "hid"
            elif key_letter == "o":
                encoded_key_letter = "g3f"
            elif key_letter == "p":
                encoded_key_letter = "yus"
            elif key_letter == "q":
                encoded_key_letter = "k87"
            elif key_letter == "r":
                encoded_key_letter = "hsf"
            elif key_letter == "s":
                encoded_key_letter = "slv"
            elif key_letter == "t":
                encoded_key_letter = "pdf"
            elif key_letter == "u":
                encoded_key_letter = "jaf"
            elif key_letter == "v":
                encoded_key_letter = "8dq"
            elif key_letter == "w":
                encoded_key_letter = "ovc"
            elif key_letter == "x":
                encoded_key_letter = "yuu"
            elif key_letter == "y":
                encoded_key_letter = "vsg"
            elif key_letter == "z":
                encoded_key_letter = "adt"
            elif key_letter == "A":
                encoded_key_letter = "tyd"
            elif key_letter == "B":
                encoded_key_letter = "0ad"
            elif key_letter == "C":
                encoded_key_letter = "iyd"
            elif key_letter == "D":
                encoded_key_letter = "tys"
            elif key_letter == "E":
                encoded_key_letter = "ytd"
            elif key_letter == "F":
                encoded_key_letter = "pvc"
            elif key_letter == "G":
                encoded_key_letter = "ofd"
            elif key_letter == "H":
                encoded_key_letter = "me3"
            elif key_letter == "I":
                encoded_key_letter = "kjj"
            elif key_letter == "J":
                encoded_key_letter = "JOJ"
            elif key_letter == "K":
                encoded_key_letter = "hsd"
            elif key_letter == "L":
                encoded_key_letter = "yub"
            elif key_letter == "M":
                encoded_key_letter = "iud"
            elif key_letter == "N":
                encoded_key_letter = "khy"
            elif key_letter == "O":
                encoded_key_letter = "hju"
            elif key_letter == "P":
                encoded_key_letter = "ghc"
            elif key_letter == "Q":
                encoded_key_letter = "cvi"
            elif key_letter == "R":
                encoded_key_letter = "ghg"
            elif key_letter == "S":
                encoded_key_letter = "5s5"
            elif key_letter == "T":
                encoded_key_letter = "huy"
            elif key_letter == "U":
                encoded_key_letter == "jhf"
            elif key_letter == "V":
                encoded_key_letter = "gvx"
            elif key_letter == "W":
                encoded_key_letter = "hjl"
            elif key_letter == "X":
                encoded_key_letter = "spo"
            elif key_letter == "Y":
                encoded_key_letter = "iax"
            elif key_letter == "Z":
                encoded_key_letter = "yuy"
            elif key_letter == " ":
                encoded_key_letter = "jmb"
            else:
                encoded_key_letter = key_letter*3

            encoded_key = encoded_key + encoded_key_letter 
        return encoded_data[:3] + encoded_key + encoded_data[3:]
    else:
        return "Invalid key"


def keyed_decrypt(data,key):
    if len(data)%3==0:
        decoded_data = ""
        for i in range(0, len(data), 3):
            encoded_letter = data[i:i+3]
            if encoded_letter == "tfe":
                letter = "1"
            elif encoded_letter == "dyu":
                letter = "2"
            elif encoded_letter == "kgh":
                letter = "3"
            elif encoded_letter == "54k":
                letter = "4"
            elif encoded_letter == "f8s":
                letter = "5"
            elif encoded_letter == "iuh":
                letter = "6"
            elif encoded_letter == "ls0":
                letter = "7"
            elif encoded_letter == "gca":
                letter = "8"
            elif encoded_letter == "paz":
                letter = "9"
            elif encoded_letter == "kfj":
                letter = "0"
            elif encoded_letter == "uxy":
                letter = "a"
            elif encoded_letter == "yua":
                letter = "b"
            elif encoded_letter == "5hq":
                letter = "c"
            elif encoded_letter == "gia":
                letter = "d"
            elif encoded_letter == "65a":
                letter = "e"
            elif encoded_letter == "v3a":
                letter = "f"
            elif encoded_letter == "oys":
                letter = "g"
            elif encoded_letter == "apa":
                letter = "h"
            elif encoded_letter == "ava":
                letter = "i"
            elif encoded_letter == "9as":
                letter = "j"
            elif encoded_letter == "ags":
                letter = "k"
            elif encoded_letter == "asg":
                letter = "l"
            elif encoded_letter == "ads":
                letter = "m"
            elif encoded_letter == "hid":
                letter = "n"
            elif encoded_letter == "g3f":
                letter = "o"
            elif encoded_letter == "yus":
                letter = "p"
            elif encoded_letter == "k87":
                letter = "q"
            elif encoded_letter == "hsf":
                letter = "r"
            elif encoded_letter == "slv":
                letter = "s"
            elif encoded_letter == "pdf":
                letter = "t"
            elif encoded_letter == "jaf":
                letter = "u"
            elif encoded_letter == "8dq":
                letter = "v"
            elif encoded_letter == "ovc":
                letter = "w"
            elif encoded_letter == "yuu":
                letter = "x"
            elif encoded_letter == "vsg":
                letter = "y"
            elif encoded_letter == "adt":
                letter = "z"
            elif encoded_letter == "tyd":
                letter = "A"
            elif encoded_letter == "0ad":
                letter = "B"
            elif encoded_letter == "iyd":
                letter = "C"
            elif encoded_letter == "tys":
                letter = "D"
            elif encoded_letter == "ytd":
                letter = "E"
            elif encoded_letter == "pvc":
                letter = "F"
            elif encoded_letter == "ofd":
                letter = "G"
            elif encoded_letter == "me3":
                letter = "H"
            elif encoded_letter == "kjj":
                letter = "I"
            elif encoded_letter == "JOJ":
                letter = "J"
            elif encoded_letter == "hsd":
                letter = "K"
            elif encoded_letter == "yub":
                letter = "L"
            elif encoded_letter == "iud":
                letter = "M"
            elif encoded_letter == "khy":
                letter = "N"
            elif encoded_letter == "hju":
                letter = "O"
            elif encoded_letter == "ghc":
                letter = "P"
            elif encoded_letter == "cvi":
                letter = "Q"
            elif encoded_letter == "ghg":
                letter = "R"
            elif encoded_letter == "5s5":
                letter = "S"
            elif encoded_letter == "huy":
                letter = "T"
            elif encoded_letter == "jhf":
                letter = "U"
            elif encoded_letter == "gvx":
                letter = "V"
            elif encoded_letter == "hjl":
                letter = "W"
            elif encoded_letter == "spo":
                letter = "X"
            elif encoded_letter == "iax":
                letter = "Y"
            elif encoded_letter == "yuy":
                letter = "Z"
            elif encoded_letter == "jmb":
                letter = " "
            else:
                letter = encoded_letter[1]
            
            decoded_data = decoded_data + letter
        

        if key == decoded_data[1:33+32]:
            return decoded_data[:1] + decoded_data[65:]
        else:
            return "Invalid key, data: " + decoded_data[3:33+32]
    else:
        return "Invalid data"
