import random
play_again = 'Y'
print "I am thinking of a number between 1 and 10."
while play_again=='Y':
    guesses_left = 5
    winner = 0
    secret_number = random.randint(1,10)
    while guesses_left:
        print "You have %d guesses left." % guesses_left
        guess = int(raw_input("What's the number?"))
        if guess == secret_number:
            print "Yes! You win!"
            winner =1
            break
        else:
            if guess<secret_number:
                print "%d is too low." % guess
            else:
                print "%d is too high." % guess
        guesses_left -=1

    if not winner:
        print "You ran out of guesses!"
    play_again = raw_input("Do you want to play again (Y or N)?").upper()
print "Bye!"
