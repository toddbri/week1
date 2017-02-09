width = int(raw_input("Width?"))
height = int(raw_input("Height?"))
# Option 1
print "*" * width
for i in range(0,height-2):
    if width>1:
        print "*" + " " * (width -2) + "*"
    else:
        print "*"

if height > 1:
    print "*" * width

print "-" * 10
# Option 2
line1 = "*" * width + "\n"
line2 = ((("*" + " " * (width -2) + "*") if width >1 else "*")+"\n") * (height-2)
line3 = "*" * width if height>1 else "\r"
print line1 + line2 + line3

print "-" * 10
# Option 3
print ("*" * width + "\n") + (((("*" + " " * (width -2) + "*") if width >1 else "*")+"\n") * (height-2)) + ("*" * width if height>1 else "")
