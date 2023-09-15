def read_words():
    wordlist = set()
    with open("/usr/share/dict/words") as file:
        for line in file:
            word = line.strip().upper()
            if len(word) == 5:
                wordlist.add(word)
    return sorted(wordlist)

# ADIEU=...eu QUEUE=QU..E # QUOTE
# LABOR=..... STINK=..i.. PITCH=.I... DIVER=dI... # GIDDY 
# SLAVE=..a.e AGENT=a.e.. MAKER=.A.ER # CAPER
# ADIEU=.d.E. CEDED=..DE. # OLDER
# ADIEU=.d.E. MODEL=.oDEl # OLDER
# ADIEU=..I.. SHINY=shI.. WHIST=WHIS. # WHISK
# ADIEU=a..e. EARTH=ear.. SHARE=..are REBAR=.e.AR # CLEAR
# ADIEU=a.... PASTA=.A... CAROL=.ArO. FAVOR=.A.Or # RAYON

def is_eligible(word, correct, absent, valid, wrong_spot):
    letters = {c for c in word}
    if (valid & letters != valid):
        return False
    if letters & absent != set():       
        return False
    for i in range(5):
        if correct[i] is not None:
            if correct[i] != word[i]:
                return False
        if word[i] in wrong_spot[i]:
            return False
    return True  

# guess_scores_multiple = ["ADIEU=...eu QUEUE=QU..E", # QUOTE
#     "LABOR=..... STINK=..i.. PITCH=.I... DIVER=dI...", # GIDDY 
#     "SLAVE=..a.e AGENT=a.e.. MAKER=.A.ER", # CAPER
#     "ADIEU=.d.E. CEDED=..DE.", # OLDER
#     "ADIEU=.d.E. MODEL=.oDEl", # OLDER
#     "ADIEU=..I.. SHINY=shI.. WHIST=WHIS."," # WHISK
#     "ADIEU=a..e. EARTH=ear.. SHARE=..are REBAR=.e.AR", # CLEAR
#     "ADIEU=a.... PASTA=.A... CAROL=.ArO. FAVOR=.A.Or"] # RAYON

# make a function out of assigning guesses to correct, present, valid, absent,wrong_spoy 
# for guess_scores in guess_scores_multiple:
# run the function on guess_scores

def parse_scores(guess_scores):
    valid = set()
    absent = set()
    correct = [None for j in range(5)]
    wrong_spot = [set() for i in range(5)]

    for guess_score in guess_scores:
        guess, score = guess_score.split('=')
        print(guess, score)
        for i in range(5):
            print(i, guess[i], score[i])
            if guess[i] == score[i]:
                valid.add(guess[i])
                correct[i] = guess[i]
            elif guess[i] == score[i].upper():
                valid.add(guess[i])
            else:
                if guess[i] not in valid:
                    absent.add(guess[i])

    print("\nvalid = ", valid, "\ncorrect = ", correct,  "\nabsent = ", absent)
    return (valid, correct, wrong_spot, absent)

guess_scores = "ADIEU=a..e. EARTH=ear.. SHARE=..are REBAR=.e.AR".split() # CLEAR
valid, correct, wrong_spot, absent = parse_scores(guess_scores)
wordlist = read_words()
for word in wordlist:
    if is_eligible(word, 
        correct = correct,
        absent = absent, 
        valid = valid,
        wrong_spot = wrong_spot):
        print(word)

