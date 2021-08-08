#given an array which contains 3 or more elements
#all made up of integers
#each array having completely odd or completely even integers, except for 1 integer
#find that outlier

#traverse each integer in the array and modulus each one by 2, 
#if there are more with a remainer of 0 or more with a remainder of greater than 0 classify array as even or odd case
#compare the length of the lists, the lesser length is the outlier
#return outlier
integerarray = [2, 4, 0, 100, 4, 11, 2602]



def find_outlier(integerarray):

    evencase = []
    oddcase = []

    for e in integerarray:
        if e%2 == 0:
            evencase.append(e)
        elif e%2 != 0:
            oddcase.append(e)
        
        
    x = len(evencase)
    y = len(oddcase)

        
    if x > y:
        print(oddcase)
            
            #return oddcase[0]
            
    
    elif y > x:
        print(evencase)
            
            #return evencase[0]
            
        
    

    #print(evencase)
    #print(oddcase)



find_outlier(integerarray) #it's working


    

