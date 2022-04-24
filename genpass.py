# ----------------------------------------------------------------------------- 
# FILE: genpasswd.py                                                            
#                                                                               
# DESC: Generate several random passwords using three different methods.  The   
#       first method provides a string of upper and lower case letters, a set   
#       of digits and special characters arranged randomly.  The second takes   
#       two random words from the English language and combines them with a     
#       number of 3-4 digits.  The third takes two 'opposite' words like hot    
#       and cold and combines them, converting some letters to numeric          
#       replacements, like 0 (zero) for O (oh), 9 for g, etc.                   
#                                                                               
# AUTH: Lawrence Nelson (Exet3r) 10 August 2019                                 
#                                                                               
# ----------------------------------------------------------------------------- 


import string
import random

import opposites

try:
    from nltk import corpus as nltk_corpus
except ImportError as err:
    print("Import Error: {}".format(err))
    print("Module nltk (Natural Language Toolkit) not available: 2 word pass omitted")
    nltk_corpus = None




# ----------------------------------------------------------------------------- 
# Global Config:                                                                
# ----------------------------------------------------------------------------- 

_PASS_COUNT = 5  # Print five samples of each password type 
_MN = 'min'
_MX = 'max'
_FRAC = 'fraction'


# ----------------------------------------------------------------------------- 
# METHOD 1:  genrandompass():                                                   
#   Randomly chosen letters, digits and special characters                      
#                                                                               
#   These values configure the random character method.  The password generated 
#   will be between 10 and 22 characters, it will contain between 1 and 5       
#   digits, etc.  Note that lower case fills any unfilled chars.                
# ----------------------------------------------------------------------------- 

_RC_PSSWD_LEN = {_MN: 10, _MX: 22}
_RC_DIGIT_CNT = {_MN: 1, _MX: 5}
_RC_SPECL_CNT = {_MN: 1, _MX: 3}
_RC_UPPER_CNT = {_MN: 2, _FRAC: 1/3}

# special = string.punctuation  ## Full set of special characters
# special = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~,"  ## All from str.punctuation 
# special = '!#$%&\()*+,-./:;<=>?@[\\]^_{|}~'  ## Remove just quotation marks 
_RC_SPECIAL = '!#$%&*+,-./:;=?@\\^_|~'  # Remove quotes, brackets 


# ----------------------------------------------------------------------------- 
# METHOD 2: gen2wordpass():                                                     
#   Two English words chosen at random plus a short integer                     
#                                                                               
#   These parameterize the two word method.  The integer of the third value     
#   will have bewteen 4 and 5 digits.                                           
# ----------------------------------------------------------------------------- 

_2W_DIGIT_CNT = {_MN: 4, _MX: 5}
_2W_DELIM_CHRS = ":;/-_.,"


# ----------------------------------------------------------------------------- 
# METHOD 3: gen2oppositepass():                                                 
#   Two words of opposite meaning, chosen at random, plus a short integer       
#                                                                               
#   These parameterize the two opposite method.  The integer of the third value 
#   will have bewteen 4 and 5 digits.                                           
# ----------------------------------------------------------------------------- 

_2O_DIGIT_CNT = {_MN: 4, _MX: 5}
_2O_DELIM_CHRS = ":;/-.,"


# ----------------------------------------------------------------------------- 
# METHOD 4: gen2oppositenbrpass():                                              
#   Two words of opposite meaning, random, obfuscated using replacement pairs   
#                                                                               
#   These parameterize the two opposite number method.  The character           
#   replacements below are used to replace some letters in the words,           
#   e.g. Onion -> 0n1on, Galley -> 6all3y, to make them more difficult to guess.
# ----------------------------------------------------------------------------- 

_2N_DELIM_CHRS = ":/-"
_CHARACTER_REPLACEMENTS = dict((pair[0], pair[1]) for pair in (
        'A4', 'a@', 'B8', 'b6', 'C<', 'E3', 'e3', 'G6', 'g9', 'i:',
        'l1', 'o0', 'O0', 'S$', 's5', 'T7', 't+', 'x%', 'Z2', 'z2',
    ))
# ------------------------------------------------------- end global config --- 



def main():
    # Main                                                                      

    print('\n\n')
    print('GENERATED PASSWORDS:')

    printpass()
    printpass('Random', genrandompass, _PASS_COUNT)
    if nltk_corpus is not None:
        printpass('2 Words', gen2wordpass, _PASS_COUNT)
    printpass('2 Opposing Words', gen2oppositepass, _PASS_COUNT)
    printpass('2 Nerfed Opposing', gen2oppositenbrpass, _PASS_COUNT)

    print('  %s\n\n\n' % ('-' * 54))

    return



# ----------------------------------------------------------------------------- 
# Utilities:                                                                    
# ----------------------------------------------------------------------------- 

def printpass(title: str = '', passwdcallable=None, count: int = -1) -> None:
    # Print 'count' outputs of the password callable in a table format          

    if count > 0:
        print('  %-20s  %s' % (title+':', passwdcallable()))
        for i in range(count-1):
            print('  %20s  %s' % (' ', passwdcallable()))
        print()
    else:
        print()
        print('  %-20s  %s' % ('TYPE', 'PASSWORD'))
        print('  %-20s  %s' % ('-'*20, '-'*32))

    return


def choose_random(charsource: str, count: int) -> list:
    # Generate a string of characters chosen at random from the character       
    # source, 'charsource', of length 'count'.                                  

    return list(random.choice(charsource) for i in range(count))


def getrandomdigits(mincount: int, maxcount: int) -> str:
    digitcount = random.randint(mincount, maxcount)
    return ''.join(choose_random(string.digits, digitcount))


def getrandomopposites() -> list:
    wordlist = list(random.choice(opposites.OPPOSITE_WORD_PAIRS))
    random.shuffle(wordlist)
    return wordlist


def obfuscateword(word: str) -> str:
    # Obfuscate the word by replacing some letters with mnemonic equivilants    
    word_list = list(word)
    indices = [(ix, ch,) for ix, ch in enumerate(word_list) if ch in _CHARACTER_REPLACEMENTS]
    if indices:
        random.shuffle(indices)
        replacecount = 1 + random.randint(0, len(indices)-1)
        for ix, ch in indices[:replacecount]:
            word_list[ix] = _CHARACTER_REPLACEMENTS[ch]
    return ''.join(word_list)
# ----------------------------------------------------------- end utilities ---




# ----------------------------------------------------------------------------- 
# Password Generators:                                                          
# ----------------------------------------------------------------------------- 


def genrandompass() -> str:
    # Generate a password of random characters made up of upper, lower letters, 
    # digits and special characters.                                            

    # Character counts / lengths.  See configuration at top. 
    length = random.randint(_RC_PSSWD_LEN[_MN], _RC_PSSWD_LEN[_MX])
    speclcount = random.randint(_RC_SPECL_CNT[_MN], _RC_SPECL_CNT[_MX])
    digitcount = random.randint(_RC_DIGIT_CNT[_MN], _RC_DIGIT_CNT[_MX])

    maxlen = int(round((length-speclcount-digitcount + 1) * _RC_UPPER_CNT[_FRAC]))
    uppercount = random.randint(_RC_UPPER_CNT[_MN], maxlen)

    # remainder of length is lower case 
    lowercount = length - uppercount - speclcount - digitcount

    lowerchars = list(choose_random(string.ascii_lowercase, lowercount))
    upperchars = list(choose_random(string.ascii_uppercase, uppercount))
    digitchars = list(choose_random(string.digits, digitcount))
    speclchars = list(choose_random(_RC_SPECIAL, speclcount))

    passwd = lowerchars + upperchars + digitchars + speclchars
    random.shuffle(passwd)
    return ''.join(passwd)


def gen2wordpass() -> str:
    # Generate a password using two English words taken from the nltk (Natural  
    # Language Toolkit) module separated by a delimiter.  Also add a number to  
    # the end between 3 and 4 digits in length.

    if nltk_corpus is None:
        return ''
    else:
        word_list = nltk_corpus.words.words()

        word0 = random.choice(word_list)
        word1 = random.choice(word_list)
        digits = getrandomdigits(_2W_DIGIT_CNT[_MN], _2W_DIGIT_CNT[_MX])
        delim = random.choice(_2W_DELIM_CHRS)

        return delim.join([word0, word1, digits])


def gen2oppositepass() -> str:
    # Generate a password using two opposing words (as listed in opposites.py)  
    # plus a number between 4 and 5 digits long.  Studies show that passwords   
    # comprised of two related words separated by a delimiter are the easiest   
    # to remember.                                                              

    word0, word1 = getrandomopposites()
    digits = getrandomdigits(_2O_DIGIT_CNT[_MN], _2O_DIGIT_CNT[_MX])
    delim = random.choice(_2O_DELIM_CHRS)

    return delim.join([word0, word1, digits])


def gen2oppositenbrpass() -> str:
    # Generate a password made of two opposing words (see opposites.txt)        
    # seperated by a delimeter.  Some letters in each word are nerfed by        
    # replacing them with a number or symbol, such as replacing 'a' with '@' or 
    # replacing 'o' with '0' (zero).  See CHARACTER_REPLACEMENTS as defined in  
    # the globals section at the top for all replacement pairs.                 

    wordlist = [obfuscateword(word) for word in getrandomopposites()]
    delimiter = random.choice(':/-')

    return delimiter.join(wordlist)
# ------------------------------------------------- end password generators ---



if __name__ == '__main__':
    main()


# ------------------------------------------------- end of file: genpass.py --- 
