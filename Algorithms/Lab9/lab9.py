weights = [2, 3, 4, 5]
values = [1, 2, 5, 6]
n = 4
W = 8
    
def AlgorithmKnapsackDP(weights, values, n, W):
    

    F = [[0 for j in range(W + 1)] for i in range(n + 1)]


    for i in range(1, n + 1):
        for j in range(W + 1):
            if weights[i - 1] > j:
                F[i][j] = F[i - 1][j]
            
            else:
                F[i][j] = max (F[i - 1][j], values[i -1] + F[i - 1][j - weights[i - 1 ]])
    
    maxValue = F[n][W]

    print("Maximum value:", maxValue)

    j = W

    for i in range(n, 0, -1):
        if F[i][j] != F[i - 1][j]:
            print("item i is included")
            j = j - weights[i - 1]
        else:
            print("item i is not included")
    
    print("\nDP Table:")
    
    for row in F:
        print(row)

AlgorithmKnapsackDP(weights, values, n, W)


