Depth-First Search (DFS) has two functions one is the main one and the other is a helper 
recursive function. Inside the recursive function it starts by marking the current 
vertex as visted and printing it then looks at every neighbor connected to this vertex 
and vists if not visted before. It then starts DFS from the first vertex and returns
every vertex visted

Breathdth-First Search (BFS) starts by visting the first goal and adding it to the 
queue then goes to a while loop that continues to loop while there are items in the 
queue and then removes the first vertex from the queue and prints the current vertex
then there is a for loop that checks the all neighboring vertices and if it has not 
been visted marked it as visted and add it to the back of the queue. then after that 
return all visted vertices.

The last part is just to test each one and calls the function and start with a