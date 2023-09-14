# this function searches /usr/share/dict/words for 5-letter words, and uses
# those words to build a list of candidates for solutions
def read_words():

# use set() to avoid duplication resulting from convergences from 
# converting everything to uppercase (example: "morse" and "Morse"
# both become "MORSE"). Initially, wordlist is an empty set.
    wordlist = set()
    with open("/usr/share/dict/words") as file:
        for line in file:

            # convert word to uppercase after removing trailing newlines to avoid double-spacing
            word = line.strip().upper()

            # if the converted word is 5 letters long, add it to candidate list
            if len(word) == 5:
                wordlist.add(word)
    
    # sort the finished collection of candidate words into a list and return it 
    return sorted(wordlist)

# ADIEU = ...eu, QUEUE = QU..E, QUOTE = QUOTE
#       and word[0] == "Q" and word[1] == "U" and word[4] == "E"
#     if is_eligible(word, absent = {'A', 'D', 'I'}, present = {'E', 'U'}):

# LABOR = ....., STINK =..i.., PITCH = .I..., DIVER = dI..., GIDDY = GIDDY 
#    absent = {'L','A','B','O','R','S','T','N','K','P','T','C','H','V','E','R'}, 
#    present = {'D', 'I'}):
# and word[1] == "I"

# SLAVE= ..a.e, AGENT= a.e.., MAKER= .A.ER, CAPER
# and word[1] == "A" and word[3] == 'E' and word[4] == 'R'
#  
# ADIEU = .d.E., CEDED = ..DE., 
# and word[2] == "D" and word[3] == 'E', OLDER = OLDER

# ADIEU = .d.E., MODEL = .oDEl, 
# and word[2] == "D" and word[3] == 'E', OLDER = OLDER

# ADIEU = ..I.., SHINY = shI.., WHIST = WHIS., WHISK = WHISK

# ADIEU = a..e., EARTH = ear.., SHARE = ..are, REBAR = .e.AR, CLEAR = CLEAR


# this function evaluates candidate words on the basis of whether it contains
# * correct letters (letters in correct position),
# * does not contain letters that should be absent,
# * contains valid letters (letters that are either correct or present), and 
# * does not contain letters that are in the wrong spot
def is_eligible(word, correct, absent, valid, wrong_spot):

    # step through each letter in the candidate word to evaluate it individually (WRONG)
    # transform word into a set of letters, and process each letter in the set in turn
    # transform word into a set of letters
    letters = {c for c in word}

    # this throws us out of the function because--if the intersection of valid
    # and letters is not just all the letters in valid, then the candidate is 
    # not a solution, and there's no need for any further checking
    # are ALL the characters in `valid` present in `letters`? Reject if not.
    if (valid & letters != valid):
        return False
    
    # if letters contains any letters that should be absent, then the candidate
    # is not a solution, and there's no need for any further checking
    # Are ANY of the characters in `absent` present in `letters`? Reject if so.
    if letters & absent != set():       
        return False
    

    # for 1 = 0, 1, 2, 3, and 4, but not 5, in turn
    for i in range(5):

        # if we know any correct letters,
        # if there is a known, correct letter at position i...
        if correct[i] is not None:
            # and if any of those correct letters is not in the correct 
            # position in the candidate word,
            if correct[i] != word[i]:
                # then we reject the word and exit the function--no more checking needed
                return False
            
        # if any letters in the word are in the wrong start (complementary to previous test),
        # then we reject the word and exit the function--no more checking needed
        # is the current character one that MUST NOT be at this position?        
        if word[i] in wrong_spot[i]:
            return False
    
    # if the word passes all of those tests, it remains a candidate and goes on the list
    return True

guess_scores = "ADIEU=a..e. EARTH=ear.. SHARE=..are REBAR=.e.AR".split() # CLEAR
valid = set()
absent = set()
for guess_score in guess_scores:
    guess, score = guess_score.split('=')
    print(guess, score)
    for i in range(5):
        print(i, guess[i], score[i])

        if guess[i] == score[i]:
            #correct
            valid.add(guess[i])
        elif guess[i] == score[i].upper():
            #present
            valid.add(guess[i])
        else:
            if guess[i] not in valid:
                absent.add(guess[i])

print(valid, absent)

# read wordlist one word at a time
wordlist = read_words()
# print(len(wordlist))

# process each word in wordlist 
for word in wordlist:

    # call the is_eligible function with word (from wordlist)
    if is_eligible(word, 
                   
                   # correct parameter, manually constructed,
                   # contains all the correct letters in solution,
                   # where correct means right letter in right position
                   # indicated in the partial solution by an uppercase letter.
                   # Green tiles on Wordle board.
                   correct = [None, None, None, 'A', 'R'],

                   # absent parameter, manually constructed, contains all 
                   # letters we have ruled out of solution, represented in 
                   # absent set by uppercase, and in the partial solution by dot.
                   # Black tiles on Wordle board.
                   absent = absent, 

                   # valid parameter, manually constructed, contains all
                   # letters that we know are in the solution: set of yellow letters
                   # plus set of green letters on Wordle board, represented in valid 
                   # set by uppercase letter.
                   # keyword valid is using parameter I just calculated, which is called valid
                   valid = valid,

                   # wrong_spot list, manually constructed, contains all
                   # letters that we know are in the solution, but that we don't know 
                   # the correct position for, although we do know where it is not
                   # in the correct solution. More than one letter can have the same
                   # incorrect position, so wrong_spot is a list of 5 sets, where
                   # each set in the list represents a position in the solution.
                   # Represented by lowercase letters in our notation, and by
                   # yellow tiles on the Wordle board.
                   wrong_spot = [{'A','E'},{'A','E'},{'A','R'},{'R','E'},{'E'}]):
        # We call is_eligible with all of these parameters, and if it passes every
        # test in is_eligible, then we print the word as a candidate for the solution.
        print(word)

