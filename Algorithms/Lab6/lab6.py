from collections import deque

graph = {
    'a': ['c', 'd'],
    'b': ['f'],
    'c': ['a', 'd', 'e', 'f'],
    'd': ['a', 'c'],
    'e': ['c'],
    'f': ['b', 'c'],
    'g': ['h'],
    'h': ['g', 'i', 'j'],
    'i': ['h'],
    'j': ['h']
}

#Depth-First Search (DFS)
def dfs(graph, start):

    visited = set()

    #helper recursive fuction
    def dfs_visit(vertex):

        #marks the current vertex as visted and prints it
        visited.add(vertex)
        print(vertex)

        #looks at every neighbor connected to this vertex and vists if not 
        #visted before
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_visit(neighbor)

    dfs_visit(start)
    return visited


#Breadth-First Search (BFS)
def bfs(graph, start):

    visited = set()
    queue = deque()

    visited.add(start) #vists the starting vertex
    queue.append(start) #add the starting vertex to the queue

    #loops while there are items in the queue and removes the first vertex
    #from the queue and prints the current vertex
    while queue:

        vertex = queue.popleft()
        print(vertex)

        #checks the all neighboring vertices and if it has not been visted
        #mark it as visted and add it to the back of the queue
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


#test DFS
print("DFS Traversal:")
dfs(graph, 'a')

#test BFS
print("\nBFS Traversal:")
bfs(graph, 'a')



# 1) What is the time complexity of DFS using an adjacency list?
    #O(V+E) V is the number of vertices and e is the number of edges 
# 2) What is the time complexity of BFS using an adjacency list?
    #O(V^2) V is the number of vertices
# 3) What would the complexity be if we used an adjacency matrix?
    # it would be O(V^2) because the algorithm must scan every row of the
    # matrix to find neighboring vertices
# 4) When would you prefer BFS over DFS?
    #when you need to find the shortest path in an unweighted graph
# 5) When would you prefer DFS over BFS?
    #when you want to explore all the paths possiable 
    