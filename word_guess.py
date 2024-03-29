"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with

def insert_value_at_index(string, value, index):
    if index < 0 or index > len(string):
        #Handle invalid index
        return string

    return string[:index] + value + string[index + 1:]
    


def replace_letter_in_dashes(status, word, letter):
    count = 0
    new_status = ''
    times_letter_in_word = word.count(letter)
    #print(times_letter_in_word)

    for i in range(times_letter_in_word):
        
        index_ocurrance = word.find(letter,count)
        lett = word[index_ocurrance]
        count += (index_ocurrance + 1)
        new_status = insert_value_at_index(status, lett, index_ocurrance)
        status = new_status
            

    return new_status


def handle_word_status(status,word,correct_letter):
    
    word_to_dashes = ''
    for i in range(len(word)):
        word_to_dashes += '-'
    
    new_status = replace_letter_in_dashes(status, word, correct_letter)

    if new_status == word_to_dashes: return status

    return new_status
    

def letter_checker(status, word, letter):
    if status == None: return 'None'
    if letter in status: return 'Repeated'
    if letter in word: return 'Correct'
    else: return 'Incorrect'


def handdle_letter_input(letter):

    if len(letter) > 1: return 'More than 1'
    if len(letter) == 0: return '0'
    ascii_order = ord(letter)
    if (ascii_order < 123 and ascii_order > 96) or (ascii_order < 91 and ascii_order > 64):
        if ascii_order < 123 and ascii_order > 96: 
            capital = letter.capitalize()
            return capital
        return letter
    
    else: return 'Incorrect'


def play_game(secret_word):
    
    count = 0
    user_count = 8
    loop_count = 0
    word_to_dashes = ''
    for i in range(len(secret_word)):
        word_to_dashes += '-'

    while True:
        
        if loop_count == 0: status = word_to_dashes
        loop_count += 1
        value = str(input('Type a single letter here, then press enter: '))

        handdle_letter = handdle_letter_input(value)
        if handdle_letter == 'Incorrect': 
            count += 1
            user_count = 8
        elif handdle_letter == 'More than 1': print('Guess should only be a single character.')
        elif handdle_letter == '0': print('insert a character')
        else:
            letter = letter_checker(status, secret_word, handdle_letter)
            if letter == 'Incorrect': 
                count += 1
                user_count -= 1
            elif letter == 'Repeated':
                print('Repeated a letter wich is a correct answer')
            elif letter == 'Correct':
                new_status = handle_word_status(status, secret_word, handdle_letter)
                status = new_status
                print('Answer correct')
                if status == secret_word: 
                    print('You win. The correct word is', status)
                    break

        if count == INITIAL_GUESSES:
            print('You lose. The correct word was', secret_word)
            break

        print('The word now looks like this:', status )    
        print('You have', user_count, 'guesses left.')   
    


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
    #create a list then choose a random item

    list = []
    with open(LEXICON_FILE, 'r') as file:

        for line in file:
            line = line.strip()
            list.append(line)
            

    rand_item = random.sample(list, k=1)
    stri = ''.join(rand_item)
    return stri


    


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