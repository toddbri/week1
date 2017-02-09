import random
def print_hangman():
    print "  ------"
    print "  |    |"
    print "  |    " + ("O" if (guesses<7) else " ")
    print "  |   " + ("\\" if (guesses <5) else " ") + ("|" if (guesses<6) else " ") + ("/" if (guesses<4) else " ")
    print "  |    " + ("|" if (guesses <3) else " ")
    print "  |   " + ("/" if (guesses <2) else " ") + " " + ("\\" if (guesses<1) else " ")
    print " ---"
    print "--------------------------------"

words =["account","address","advance","auction","brother",
        "cabinet","captain","holding","install","instant","visible","advisor",
        "aborted","bracket","builder","crimson","custard","fixture"]
word = words[int(random.randint(0,len(words)-1))]
original_word=word
# print "the word is:", word
guesses = 7
strguesses = ""
wip = "_ _ _ _ _ _ _ "
winner =0
print "Welcome to Hangman. I have a word can you guess it?"
while guesses>0:
    guess = raw_input("What is your guess(" + strguesses[1:] + ")?")
    found = word.find(guess)
    if found ==-1:
        guesses -=1
        strguesses +="," + guess
        print "Nope, you have " + str(guesses) + " left"
    else:
        while word.find(guess)>-1:
            found = word.find(guess)
            word = word[:found] + "*" + word[found+1:]
            wip = wip[:found*2] + guess + wip[found*2+1:]
        if (word == "*"*7):
            guesses=0
            winner = 1
        if not winner:
            print "Good guess, you have " + str(guesses) + " left"
    print wip
    if not winner:
        print_hangman()

if winner:
    print "Yeah, you are a winner."
else:
    print "You are out of guesses....you lose."
    print "The word is: ", original_word
