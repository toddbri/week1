list = [1,5,-8,8,5,4.5,6,7,5,1,-8]
#list = ["alpha","beta","gamma","beta","delta","alpha"]
print str(list) + " =>",
out_list=[]
dups=[]
for item in list:
    if not (item in out_list):
        out_list.append(item)
    else:
        if not (item in dups):
            dups.append(item)
print str(out_list)
print "dups removed: " + str(dups)
