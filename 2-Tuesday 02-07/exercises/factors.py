num = int(raw_input("What is your number?"))
for i in range(1,num+1):
    if not num%i:
        print i
