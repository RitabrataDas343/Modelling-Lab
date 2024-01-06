from shapely.geometry import LineString
from matplotlib import pyplot as plt

# Labels for the plot
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.title('Plotting')

# For points in equation 1
x1 = [250,0]
y1 = [0, 500]
plt.plot(x1, y1)

# For points in equation 2
x2 = [0,250]
y2 = [250, 250]
plt.plot(x2, y2)

# For points in equation 3
x3 = [150,150]
y3 = [0, 500]
plt.plot(x3, y3)

# Plotting the three lines
line1 = LineString([(250, 0),(0, 500)])
line2 = LineString([(150, 0),(150, 500)])
line3 = LineString([(0, 250),(250, 250)])

# Finding the intersection of the points
intersection = line1.intersection(line3)
plt.plot(*intersection.xy, 'ro')
intersection2 = line1.intersection(line2)
plt.plot(*intersection2.xy, 'go')
plt.plot(0,250,'bo')
plt.plot(150,0,'mo')
p1, q1 = intersection.xy
p2, q2 = intersection2.xy

# Appending the points in two list having the x and y co-ordinates
x = []
y = []
x.append(0)
x.append(p1[0])
x.append(p2[0])
x.append(150)
y.append(250)
y.append(q1[0])
y.append(q2[0])
y.append(0)

# Filling the common region formed by the lines
plt.fill_between(x,y, color='blue',alpha=0.2)
plt.text(50,400,"2x + y = 500")
plt.text(150, 400,"x = 150")
plt.text(50, 250,"y = 250")

# Showing the point of intersections
print("Point of Intersection 1: ")
print(p1[0])
print(q1[0])
print("Point of Intersection 2: ")
print(p2[0])
print(q2[0])

# Storing the values of objective function
z = []
for i in range(0,4):
    eqn = 8*x[i] + 5*y[i]
    z.append(eqn)
print("Z = ",z)

# Finding the optimal Solution
max_val = max(z)
xy_index = z.index(max_val)
print("The Value of Z = ",max_val," at point (",x[xy_index],",",y[xy_index],")")