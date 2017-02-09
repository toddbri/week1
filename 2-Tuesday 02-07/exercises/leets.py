paragraph = raw_input("What is your string?")
leets ={"a":"4", "e":"3","g":"6","i":"!", "o":"0", "s":"5","t":"7","l":"1"}
print paragraph + "=>",
for key in leets:
    paragraph= paragraph.replace(key,leets[key])
    paragraph=paragraph.replace(key.upper(),leets[key])
print paragraph
