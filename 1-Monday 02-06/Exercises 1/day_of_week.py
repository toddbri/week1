day = -1
while ((day<0) | (day >6)):
    try:
        day = int(raw_input('Day (0-6)? '))
    except:
        day = -1
if day == 0:
    print "Sunday"
elif day == 1:
    print "Monday"
elif day == 2:
    print "Tuesday"
elif day == 3:
    print "Wednesday"
elif day ==4:
    print "Thursday"
elif day == 5:
    print "Friday"
else:
    print "Saturday"
