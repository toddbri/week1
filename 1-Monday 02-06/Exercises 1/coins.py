coins = 0
more_coins='yes'
while more_coins=='yes':
    print "You have %d coins." % coins
    more_coins = raw_input("Do you want another?")
    coins +=1
print "Bye"
