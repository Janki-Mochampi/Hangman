# Problem Set 2, hangman.py
# Name: JANKI MOCHAMPI
# Collaborators:
# Time spent:2 days

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if secret_word == letters_guessed:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s = []
    for i in secret_word:
        if i in letters_guessed:
            s.append(i)
    ans = ''
    for i in secret_word:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    ans = list(string.ascii_lowercase)
    for a in ans[:]:
        ans = list(string.ascii_lowercase)
    for i in letters_guessed:
        ans.remove(i)
    return ''.join(ans)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_unique = []  # for secret_word deduplication

    for i in secret_word:

        if i not in list_unique:
            list_unique.append(i)
    unique_numbers = len(list_unique)

    vowels = " aeiou"
    # vowel letters

    print("Welcome to the game of hangman!")
    print("I am thinking a word that is", str(len(secret_word)), "long.")
    ##########################################################print(secret_word)
    warnings = 3
    guesses = 6
    letters_guessed = ''
    while not is_word_guessed(secret_word, letters_guessed):
        #        checking that user has guesses left
        if guesses <= 0:
            break
        elif get_guessed_word(secret_word, letters_guessed) == secret_word:
            break
        else:
            #           checking if we have to remove a guess
            if warnings == 0:
                guesses -= 1
                warnings = 3
            print("---------")
            print("You have", str(guesses), "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            user_guess = input("Please guess a letter:")
            #           checking that the input is a valid letter
            if len(user_guess) != 1 or user_guess not in list(string.ascii_lowercase):
                warnings -= 1
                print("Oops! That is not a valid letter!", "You have", warnings, "warnings left.")
            elif user_guess in letters_guessed:
                warnings -= 1
                print("Oops! That letter has alredy been guessed. You now have", warnings,
                      "warnings left.")
            #           checking if the guess is right or wrong
            elif user_guess in secret_word:
                letters_guessed += user_guess
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            
            else:
                letters_guessed += user_guess
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if user_guess in vowels:
                    guesses -= 2
                else:
                    guesses -= 1

    if guesses <= 0:
        print("Sorry, you ran out of guesses. The word was:", secret_word)
    else:

     print("Congratulations, you won!")
    total_score = guesses * unique_numbers

    print("Your total score for this game is:", total_score)

    return



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num = 0
    my_word = my_word.replace(' ', '')
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == '_' or my_word[i] == other_word[i]:
                pass
            else:
                num += 1
        if num == 0:
            return True
        else:
            return False
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            list.append(word)

    if len(list) != 0:
        print(' '.join(list))
    else:
        print('No matches found')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_unique = []  # for secret_word deduplication

    for i in secret_word:

        if i not in list_unique:
            list_unique.append(i)
    unique_numbers = len(list_unique)

    vowels = " aeiou"
    # vowel letters

    print("Welcome to the game of hangman!")
    print("I am thinking a word that is", str(len(secret_word)), "long.")
   ###################################################### print(secret_word)
    warnings = 3
    guesses = 6
    letters_guessed = ''
    while not is_word_guessed(secret_word, letters_guessed):
        #        checking that user has guesses left
        if guesses <= 0:
            break
        elif get_guessed_word(secret_word, letters_guessed) == secret_word:
            break
        else:
            #           checking if we have to remove a guess
            if warnings == 0:
                guesses -= 1
                warnings = 3
            print("---------")
            print("You have", str(guesses), "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            user_guess = input("Please guess a letter:")
            #           checking that the input is a valid letter


            if len(user_guess) != 1 or user_guess not in list(string.ascii_lowercase):
                warnings -= 1
                print("Oops! That is not a valid letter!", "You have", warnings, "warnings left.")
            elif user_guess in letters_guessed:
                warnings -= 1
                print("Oops! That letter has alredy been guessed. You now have", warnings,
                      "warnings left.")
            #           checking if the guess is right or wrong
            elif user_guess in secret_word:
                letters_guessed += user_guess
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))

            else:
                letters_guessed += user_guess
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if user_guess in vowels:
                    guesses -= 2
                else:
                    guesses -= 1

            if user_guess == '*':

             my_word = get_guessed_word(secret_word, letters_guessed)

             show_possible_matches(my_word)

    if guesses <= 0:
        print("Sorry, you ran out of guesses. The word was:", secret_word)
    else:

        total_score = guesses * unique_numbers

        print("Congratulations, you won!")


        print("Your total score for this game is:", total_score)

    return


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
