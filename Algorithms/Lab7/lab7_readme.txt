the first part is a function that implments the lomunto partition algorithm by first
selecting the first element as the pivot then keeping track of the last element.
then I use a for loop to compare every element to the pivot and sort/place the pivot in the 
correct position. Next I swap elements that are smaller to the left and print the 
array now that the pivot and the smaller elements have been sorted.  

NOTE: I was not able to finish the implention of the quickselect function in time but
this is how I would implent it if I had more time to complete the lab.

Quickselect function first checks if there is only one element left in the current 
section of the array. Then calls the partition function to place the pivot in its 
correct position. If the pivot is the smallest element the function returns it. 
If not it recursively searches either the left or right side of the array
depending on where the smallest element can be found.

