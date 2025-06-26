import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
points = []

for i in range(n):
    x = int(data[2 * i + 1])
    y = int(data[2 * i + 2])
    points.append((x, y))

points.sort(key=lambda point: (point[1], point[0]))

for x, y in points:
    print(x, y)
