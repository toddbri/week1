list1 = [[1,3],[2,4,5],[8,9]]
list2 = [[5,2],[1,0,-3],[6,7]]
list3 =[]
print str(list1) + " + " + str(list2) + " =",
for i in range(len(list1)):
    sub_element =[]
    for j in range(len(list1[i])):
        sub_element.append(list1[i][j] + list2[i][j])
    list3.append(sub_element)
print str(list3)
