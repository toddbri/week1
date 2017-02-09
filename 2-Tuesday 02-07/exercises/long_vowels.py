word = raw_input("What is your word?")
print word + " =>",
for pairs in ("aa","ee","ii","oo","uu"):
    word = word.replace(pairs,pairs[1]*5)
print word
