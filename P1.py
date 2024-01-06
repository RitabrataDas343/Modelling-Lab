from shapely.geometry import LineString
from matplotlib import pyplot as plt

# Labels for the plot
plt.xlabel('X - Axis')  
plt.ylabel('Y - Axis')
plt.title('Plotting')

# For points in equation 1
x1 = [0,2] 
y1 = [10, 0]
plt.plot(x1, y1) 

# For points in equation 2
x2 = [0, 6]
y2 = [6, 0]
plt.plot(x2, y2) 

# For points in equation 3
x3 = [0, 12]
y3 = [3, 0]
plt.plot(x3, y3) 

# Plotting the three lines
line1 = LineString([(2, 0),(0, 10)]) 
line2 = LineString([(6, 0),(0, 6)])
line3 = LineString([(0, 3),(12, 0)])

# Finding the intersection of the points
intersection = line1.intersection(line2)
plt.plot(*intersection.xy, 'ro')
intersection2 = line2.intersection(line3)
plt.plot(*intersection2.xy, 'go')
plt.plot(0,10,'bo')
plt.plot(12,0,'mo')
p1, q1 = intersection.xy
p2, q2 = intersection2.xy

# Appending the points in two list having the x and y co-ordinates
x = []
y = []
x.append(0)
x.append(p1[0])
x.append(p2[0])
x.append(12)
y.append(10)
y.append(q1[0])
y.append(q2[0])
y.append(0)

# Filling the common region formed by the lines
plt.fill_between(x,y,max(y), color='blue',alpha=0.2)
plt.text(0.8,8,"5x + y = 10")
plt.text(3,4,"2x + 2y = 12")
plt.text(8,1.5,"x + 4y = 12")

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
    eqn = 3*x[i] + 2*y[i]
    z.append(eqn)
print("Z = ",z)

# Finding the optimal Solution
min_val = min(z)
xy_index = z.index(min_val)
print("The Value of Z = ",min_val," at point (",x[xy_index],",",y[xy_index],")")