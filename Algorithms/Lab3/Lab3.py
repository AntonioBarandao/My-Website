


text = 'HELLO WORLD'

string = 'WORLD'

#loops through each position in the text
for i in range(len(text)):
    match = True
    j = 0

    #Compare characters while:
    # 1. We haven't reached the end of the pattern
    # 2. No mismatch has been found
    while j < len(string) and match:
       
        # Compare the current character in the text with 
        # the current character in the pattern
        if text[i + j] != string[j]:
            match = False
        j += 1
            
    # If match is still True after checking all characters,
    # the pattern was found starting at index i
    if match == True:
        print("Match found at index", i)
        

  