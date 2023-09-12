def read_words():
    wordlist = set()
    with open("/usr/share/dict/words") as file:
        for line in file:
            word = line.strip().upper()
            if len(word) == 5:
                wordlist.add(word)
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


def is_eligible(word, correct, absent, valid):
    letters = {c for c in word}
    if (valid & letters != valid
            or letters & absent != set()):       
        return False
    for i in range(5):
        if correct[i] is not None:
            if correct[i] != word[i]:
                return False 
    return True
    
wordlist = read_words()
# print(len(wordlist))
for word in wordlist:
    if is_eligible(word, 
                   correct = [None, None, 'D', 'E', None],
                   absent = {'A','I','U','C'}, 
                   valid = {'D', 'E'}):
        print(word)
