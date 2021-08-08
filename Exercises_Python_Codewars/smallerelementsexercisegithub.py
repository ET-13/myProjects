myarray = [1, 3, 2, 4, 6, 5, 7, 9, 9, 10, 11] #some array with unordered numerical elements
x = 10 #some value used to traverse through the elements of array up to its value

def getSmaller(myarray, x): #pass arguments to the function
    res = [] #init empty array to hold our output
    for e in myarray: #for arbitrary variable in array
        if e < x: #arbitrary variable equal to zero, less than 10, append each element until value of x reached (10)

            res.append(e)

    return res #return it


print(getSmaller(myarray,x)) #print to console

#same boilerplate for isogram


