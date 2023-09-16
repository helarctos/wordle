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
# ADIEU=...e. BERET=.ereT GREEt=.rEeT #EXERT

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

def parse_scores(guess_scores):
    valid = set()
    absent = set()
    correct = [None for j in range(5)]
    wrong_spot = [set() for i in range(5)]

    for guess_score in guess_scores:
        guess, score = guess_score.split('=')
        for i in range(5):
            print(i, guess[i], score[i])
            if guess[i] == score[i]:
                valid.add(guess[i])
                correct[i] = guess[i]
            elif guess[i] == score[i].upper():
                valid.add(guess[i])
                wrong_spot[i].add(guess[i])
            else:
                if guess[i] not in valid:
                    absent.add(guess[i])

    print("\nvalid = ", valid, "\ncorrect = ", correct,  "\nabsent = ", absent, "\nwrong_spot = ", wrong_spot)
    return (valid, correct, wrong_spot, absent)

def find_answers(wordlist, guess_scores):
    valid, correct, wrong_spot, absent = parse_scores(guess_scores)
    for word in wordlist:
        if is_eligible(word, 
            correct = correct,
            absent = absent, 
            valid = valid,
            wrong_spot = wrong_spot):
            print(word)

# guess_scores_multiple = ["ADIEU=...eu QUEUE=QU..E", # QUOTE
#     "LABOR=..... STINK=..i.. PITCH=.I... DIVER=dI...", # GIDDY 
#     "SLAVE=..a.e AGENT=a.e.. MAKER=.A.ER", # CAPER
#     "ADIEU=.d.E. CEDED=..DE.", # OLDER
#     "ADIEU=.d.E. MODEL=.oDEl", # OLDER
#     "ADIEU=..I.. SHINY=shI.. WHIST=WHIS.", # WHISK
#     "ADIEU=a..e. EARTH=ear.. SHARE=..are REBAR=.e.AR", # CLEAR
#     "ADIEU=a.... PASTA=.A... CAROL=.ArO. FAVOR=.A.Or", # RAYON

games = {
    "QUOTE": "ADIEU=...eu QUEUE=QU..E",
    "GIDDY": "LABOR=..... STINK=..i.. PITCH=.I... DIVER=dI...",
    "CAPER": "SLAVE=..a.e AGENT=a.e.. MAKER=.A.ER",
    "OLDER": "ADIEU=.d.E. CEDED=..DE.",
    "OLDER": "ADIEU=.d.E. MODEL=.oDEl",
    "WHISK": "ADIEU=..I.. SHINY=shI.. WHIST=WHIS.",
    "CLEAR": "ADIEU=a..e. EARTH=ear.. SHARE=..are REBAR=.e.AR",
    "RAYON": "ADIEU=a.... PASTA=.A... CAROL=.ArO. FAVOR=.A.Or",
    "EXERT": "ADIEU=...e. BERET=.ereT GREEt=.rEeT"
}

wordlist = read_words()
for answer, guess_scores in games.items():
    find_answers(wordlist, guess_scores.split())
    print(answer, guess_scores)
    print("=" * 75)
