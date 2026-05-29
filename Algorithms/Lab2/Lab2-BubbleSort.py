Numbers = [2,3,38,48,9,36,37,49,10,11,12,50]

i = 0

while i < len(Numbers):
 #compares from the begining
    j = 0

    while j < len(Numbers) - 1:
     #inner loop compares neigboring values

      # If left number is bigger than right number, Swap them
        if Numbers[j] > Numbers[j + 1]:
            
            # Store left value temporarily
            sort = Numbers[j]
            Numbers[j] = Numbers[j + 1]  # Move right value to left position
            Numbers[j + 1] = sort

        j += 1

    i += 1

print(Numbers)