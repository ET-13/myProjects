

book = input("enter name of txt file to search: ")
print("How many words would you like to search for? (enter an integer)")
amount = int(input())

arrayhold = []


n = 0
while(n<amount):

    data = [amount]
    


    

    
    word = input("enter word to search: ")
    count = 0
    with open("{}.txt".format(book),"r") as f:
        for line in f:
            words = line.split()
            for i in words:
                if(i==word):
                    count=count+1
                    arrayhold.append(count)
                
                    
                    


                   
                    

                   

    print("'",word,"'", "occurs", count, "times")   
    n=n+1


    


