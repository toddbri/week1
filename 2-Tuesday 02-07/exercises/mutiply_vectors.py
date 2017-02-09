list1 = [2,4,5]
list2 = [2,3,6]
list3 =[]
print str(list1) + " x " + str(list2) + " =",
for i in range(len(list1)):
        list3.append(list1[i]*list2[i])
print str(list3)
