h = int(raw_input("How high?"))
l = 1
for i in range(0,h):
    print " " * h + "*" * l
    h -=1
    l +=2
