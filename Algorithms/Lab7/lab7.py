# Lomuto Partition (First element as pivot)
def partition(array, left, right):

    # Choose the first element as the pivot then keeps track of last element 
    pivot = array[left]

    Last_element = left

    # Compare every element with the pivot, then puts the pivot into its correct position
    for i in range(left + 1, right + 1):

        if array[i] < pivot:
            Last_element += 1
            holder = array[Last_element]
            array[Last_element] =  array[i]
            array[i] = holder
    
    #swaps elements that are smaller to the lefts
    temp = array[left]
    array[left] = array[Last_element]
    array[Last_element] = temp

    print("Piviot = 4", array)

    return Last_element


# Quickselect
def quickselect(array, left, right, k):

    # Base case
    if left == right:
        return array[left]




# Test Case 1
array = [4, 1, 10, 8, 7, 12, 9, 2, 15]
k = 5

print("Original array:", array)


print("The smallest element is, ")