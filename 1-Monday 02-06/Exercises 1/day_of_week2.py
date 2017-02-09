day = -1
days = ["Sunday", "Monday", "Tuesday","Wednesday","Thursay","Friday", "Saturday"]
while ((day<0) | (day >6)):
    try:
        day = int(raw_input('Day (0-6)? '))
    except:
        day = -1
print days[day]
