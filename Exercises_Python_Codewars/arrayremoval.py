#two arrays
#array_diff function applied to them
#see what elements are shared between the arrays, ***if any
#remove those shared elements, each occurence, maintaining original order



def array_diff(myarray1, myarray2):
    result = myarray1
    for elements in myarray2:
        while elements in myarray1:

            myarray1.remove(elements)
            result = myarray1

#print(result)
    return result




    


    
