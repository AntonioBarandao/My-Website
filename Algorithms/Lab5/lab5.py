points = [(1, 1),(3, 4),(2, 4),(3, 2),(5, 3)]

n = len(points)

#check every pair of points 
for i in range(n):
    for j in range(i + 1, n):

        x1, y1 = points[i]
        x2, y2 = points[j]
        
        # Calculate the line equation ax + by = c
        a = y2 - y1
        b = x1 - x2
        c = x1 * y2 - y1 * x2

        pos = 0
        neg = 0

        #checks all other points
        for k in range(n):

            #skips points used to create the same line
            if k == i or k == j:
                continue

            x, y = points[k]

            #detirmines which side of the line the point is on
            value = a * x + b * y - c

            if value > 0:
                pos += 1
            elif value < 0:
                neg += 1

        if pos == 0 or neg == 0:
            print(points[i], "->", points[j])