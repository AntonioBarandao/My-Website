def distribution_counting_sort(A, lowest, highest):

    n = len(A)

    #counting array
    D = [0] * (highest - lowest + 1)

    #sorted array
    S = [0] * n


    #count the frequency of each value
    for i in range(n):
        D[A[i] - lowest] += 1

    print("Frequency Of Array D:")
    print(D)
    
    #finds the distribution of array D
    for j in range(1, len(D)):
        D[j] = D[j] + D[j - 1]

    print("Distribution Of Array D:")
    print(D)

    #sorts the numbers and places them in a array S
    for i in range(n - 1, -1, -1):
        j = A[i] - lowest
        S[D[j] - 1] = A[i]
        D[j] = D[j] - 1    
    return S



A = [13, 11, 12, 13, 12, 12]
lowest = 11
highest = 13

print("Original Array:")
print(A)

sorted_array = distribution_counting_sort(A, lowest, highest)

print("Sorted Array:")
print(sorted_array)