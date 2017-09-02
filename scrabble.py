'''this is a program designed to help a person win in a game of scrabble based 
on the letters he or she may have.'''

import argparse

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}#dictionary for letter values
    
def score_a_word(word):
    """This function will go through each letter in a
    word and score the word based on the value of each
    letter."""
    score = 0
    for letter in word:#links to the lower nested loops
        score += scores[letter]#adds the value for each key (letters in the words)
    return score

parser=argparse.ArgumentParser(description='designed to help in scrabble')
parser.add_argument("rack",help="input your letters")
args=parser.parse_args()
rack = args.rack.lower() #lower case it

print('the rack is: ' + rack)#prints the user input for the rack

#opens the text file and puts each word into a list for list comprehension
wordlist=[]
with open ('sowpods.txt','r') as f:
    for line in f:
        u=str.lower(line)
        wordlist.append(u.strip())

#TODO: This could be a standalone function
#TODO: Look into python `sets`; the set difference
# operator could be a cool way to do this loop
validwords=[]
for word in wordlist:
    is_valid_word = True
    temp_rack = rack
    for letter in word:
        if letter not in temp_rack:
            is_valid_word = False
            break
        else:
            #Simplistic way to deal with repeat characters
            #in word and rack...kind of inefficient
            temp_rack = temp_rack.replace(letter,"",1)
    if is_valid_word:
        validwords = validwords +  [word]

#Applied the scoring algorithm here; were
# not doing that before...
for validword in validwords:
    print(score_a_word(validword), validword)