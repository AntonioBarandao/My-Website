

points = [(1, 1), (4, 5), (2, 2), (10, 8)]

minDistance = float('inf')  #sets the min distance to infinity
closestPair = None

for i in range(len(points)):  #loops through each point in the list
    for j in range(i + 1, len(points)): # Compares the current point with every point after it
        
        p1 = points[i]
        p2 = points[j]

        # Calculate the squared distance between p1 and p2
        # (x2 - x1)^2 + (y2 - y1)^2
        distance = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
        
        #checks if the distance is the smallest one so far
        if distance < minDistance:
            minDistance = distance
            closestPair = (p1, p2)
            
print("Closest pair:", closestPair)
print("Squared distance:", minDistance)