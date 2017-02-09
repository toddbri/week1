amount = float(raw_input("Total bill amount?"))
los = raw_input("Level of service?")
LOS ={"good": .2,"fair": .15, "bad": .1}
if los == "good":
    tip = amount * .2
elif los == "fair":
    tip = amount * .15
else:
    tip = amount * .1
tip = LOS[los] * amount
tip = {"good": .2,"fair": .15, "bad": .1}[los]*amount
print "Tip amount: $%-5.2f"% tip
print "Total amount: $%-5.2f" % float(tip + amount)
