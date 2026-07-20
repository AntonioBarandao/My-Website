First i have a for loop that counts how many numbers are the same in the array then it finds
the distribution value by taking the number of times a number appears and adding it.
Ex(1,3,2  --> 1+3 = 4 --> 1,4,2  4+2=6 --> 1,4,6). This is where each number needs to end meaning
if you one 11, three 12's and 2 13's the 11 should end by position 1 and 12 should end by position 4
etc. Next using the distribution array i sort and place the numbers in a different array.




Questions to Answer
• What is the purpose of array D?
the purpose of array D is to keep track how many times each number appears in the original array
and helps detrime the position of each number in the sorted array

• Why does the algorithm first count frequencies and then convert them into distribution values?
the algorithm counts the frequencies first so it knows how many time each element appears thus 
telling what position it goes in the sorted array

• Why does the last loop go from n - 1 downto 0?
the array counts backwards so that duplicate values are in the correct order.

• Under what condition is this algorithm efficient?
The algorithm is efficient when the range of values is small when compared to the number
of elements. If the range was larger it would need a bigger counting array making it less efficient

• What is the time complexity when the range of values is fixed?
the complexity is O(n) because the algorithm only needs to run through the array a couple of times
each being a linar time