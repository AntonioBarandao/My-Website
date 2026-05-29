Numbers = [2,3,38,48,9,36,37,49,10,11,12,50]

i = 0
key = 11
Found = False

#while loop to go through the list to find the key
while i < len(Numbers):
    
    if Numbers[i] == key: # if key is found print the index and key value
        Found = True
        print('Key was found at index', i) 
        print('The key is' , Numbers[i])

    i += 1

if Found == False: # if key is not found print "key not found"
    print('Key not found')