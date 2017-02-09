ma = [[1,2,3,8],[6,2.5,3,3],[1,-2,-4,5]]
mb = [[7,8],[8,9],[9,-4],[5,5]]
ma = [[1,2,4],[5,3,8],[4,6,9]]
mb = [[2,4,5],[9,8,7],[3,1,6]]
mc =[]
if not (len(ma[0])==len(mb)):
    print "matrix dimensions are not valid for multiplication"
else:
    for i in range(len(ma)):
        elements =[]
        for j in range(len(mb[i])):
            element =0
            for k in range(len(ma[j])):
                #print str(ma[i][k]) + " * " + str(mb[k][j])
                element +=ma[i][k] * mb[k][j]
            #print element
            elements.append(element)
        #print elements
        mc.append(elements)
    print mc
