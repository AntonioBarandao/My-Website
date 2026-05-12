Sieve= [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21
        ,25,26,27,28,29,30,31,33,35,50,56,57,58,59,60,61,62
        ,63,64,65,66,67,68,69,70,71,72,73,74,88,89,90,91,92,93,96,97,98,99,100
]

i = 0

#uses two while loops and goes through each number to see
#if number is prime by moding the numbers to see if their is a remainder
while i < len(Sieve):
    p = Sieve[i] #selects curent number
    j = i + 1
    while j < len(Sieve):
        if Sieve[j] % p == 0: #checks if the number is prime
            Sieve.pop(j) 
        else:
            j += 1
    i += 1
print (Sieve)

        