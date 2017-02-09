h = int(raw_input("How high?"))
l = 1
for i in range(h,0,-1):
    print " " * i + "*" * l
    l +=2
