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
word = "account"
print "the word is:", word
guesses = 7
wip = "_ _ _ _ _ _ _ "
winner =0
while guesses>0:
    guess = raw_input("What is your guess?")
    found = word.find(guess)
    if found ==-1:
        guesses -=1
        print "nope, you have " + str(guesses) + " left"
    else:
        wip = wip[:found*2] + guess + wip[found*2+1:]
        word = word[:found] + "*" + word[found+1:]

        if (word == "*"*7):
            guesses=0
            winner = 1
        print "good guess, you have " + str(guesses) + " left"
    print wip
    if not winner:
        print_hangman()

if winner:
    print "Yeah, you are a winner"
else:
    print "You are out of guesses....you loose"
