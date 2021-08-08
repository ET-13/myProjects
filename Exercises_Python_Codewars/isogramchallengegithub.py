


#an isogram is a word which has no repeating letters 

letterdictionary = {
    "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7,
    "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, 
    "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" :25, "z" : 26,
    "A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7,
    "H" : 8, "I" : 9, "J" : 10, "K" : 11, "L" : 12, "M" : 13, "N" : 14, 
    "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21, "V" : 22, "W" : 23, "X" : 24, "Y" :25, "Z" : 26
} #each letter is associated with a number, both upper and lower for case insensitivity 





mystring = str(input("type in the string to test for isogram:"))#we take a given string #for checking isogram as a program, configuring for codewars test

myarrayofelements = list(mystring) #we convert it to an array and separate each letter to its own element

#def traverseString 
#print("test")

#mystring = "zf" #str(input("type string")) #our string input

#myarrayofelements = list(mystring)

def is_isogram(myarrayofelements): #pass arguments to the function
    
    result = [] #init empty array to hold our output
    for e in myarrayofelements: #for arbitrary variable in array
        if e in letterdictionary: #e becomes whatever the array is, the given letters are compared and their number Id from dict is returned
            
            result.append(letterdictionary[e])
            
            #print(result)
            

    def check_isogram(result):

        if len(result) != len(set(result)):
                    
            print("your word is not an isogram")
            
            return False      
                 
           
                                
        else: 
                    
            print("your word is an isogram")
                 
            return True
            

    return check_isogram(result) #using return or else nonetype error will occur implicitly



            
    

           
is_isogram(myarrayofelements)

#is_isogram("Dermalgolyphicsz")











