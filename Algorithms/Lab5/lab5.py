points = [
    (1, 1),
    (3, 4),
    (2, 5),
    (3, 2),
    (5, 3)
]

n = len(points)

print("Convex Hull Edges:")

for i in range(n):
    for j in range(i + 1, n):

        x1, y1 = points[i]
        x2, y2 = points[j]

        a = y2 - y1
        b = x1 - x2
        c = x1 * y2 - y1 * x2

        pos = 0
        neg = 0

        for k in range(n):

            if k == i or k == j:
                continue

            x, y = points[k]

            value = a * x + b * y - c

            if value > 0:
                pos += 1
            elif value < 0:
                neg += 1

        if pos == 0 or neg == 0:
            print(points[i], "->", points[j])