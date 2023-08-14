import re

def alphabet_position(text):
    
    #take string, regex it and condense
    regex = re.compile('[^a-zA-Z]')
    text = regex.sub('',text)
    #test if it is valid input, return ('') if not
    if text.isalpha(): 
         
        #make sure every character is lower   
        text = text.lower()
        
    
        #init list
        textlist = []
        #iterate through length of input string for each character
        for i in range(len(text)):
            for letter in text:
                
                #append to list as number with unicode and shift to correct placement, i.e. a = 1 
                alphatext = textlist.append((ord(letter)-96))
                
            #return elements of list as string, space-separated    
            return(' '.join(map(str,textlist)))
        
    else:
        return('')
