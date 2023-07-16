"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def replace_letter_in_dashes(status, word, letter):
    count = 0
    times_letter_in_word = word.count(letter)

    for i in range(times_letter_in_word):

        index_ocurrance = word.find(letter,)
        status[index_ocurrance] = letter




def handle_word_status(status,word,correct_letter):
    
    word_to_dashes = ''
    for i in range(len(word)):
        word_to_dashes += '-'


    for i in range(len(word)):

        if status == word_to_dashes: return 'Empty'
        else:
            newstatus = replace_letter_in_dashes()
            return newstatus

        ############
    

def letter_checker(word, letter):
    if letter in word: return 'Correct'
    ############
    

def handle_letter_input(letter):

    ascii_order = ord(letter)

    if len(letter) > 1: return False

    if (ascii_order < 123 and ascii_order > 96) or (ascii_order < 91 and ascii_order > 64):
        if ascii_order < 123 and ascii_order > 96: 
            capital = letter.capitalaize()
            return capital
        return letter
    
    else: return 'Incorrect'
    
            
    


def play_game(secret_word):
    
    word_to_dashes = ''
    while True:

        for i in range(len(secret_word)):
            word_to_dashes += '-'
        
    print('The word now looks like this:', )       
    


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randrange(3)
    if index == 0:
        return 'HAPPY'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER'


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()