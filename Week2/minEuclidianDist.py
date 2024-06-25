def euclideanDistance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def minEuclideanDistance(points, distances):
	for i in range(len(points)):
		print("x1: ", points[i][0], "y1: ", points[i][1])
		for j in range(i+1, len(points)):
			print("x2: ", points[j][0], "y2: ", points[j][1])
			print("Distance: ", euclideanDistance(points[i], points[j]))
			distances.append(euclideanDistance(points[i], points[j]))
	return min(distances)

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
distances = []
print("Min Euclidean Distance: ", minEuclideanDistance(points, distances))