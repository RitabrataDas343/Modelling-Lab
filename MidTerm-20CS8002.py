from shapely.geometry import LineString
from matplotlib import pyplot as plt

print("Name: Ritabrata Das\nRoll Number: 20CS8002\n")

#Axis Labelling
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("lab-exam")

#Point 1
plt.plot(0, 0) 

#Point 2
plt.plot(0, 10)

#Point 3
plt.plot(15, 0)

#Plotting 3 lines
line1 = LineString([(15, 0),(15, 5000)])
line2 = LineString([(0, 10),(5000, 10)])
line3 = LineString([(0, 16),(24, 0)])

#StorinG and ploting the intersection of points
intersection1 = line3.intersection(line1)
plt.plot(*intersection1.xy, 'ro')
intersection2 = line3.intersection(line2)
plt.plot(*intersection2.xy, 'go')

p1, q1 = intersection1.xy
p2, q2 = intersection2.xy

plt.plot(p1, q1)
plt.plot(p2, q2)

#Appending the points in the x and y co-ordinates list
x = []
y = []
x.append(0)
x.append(p1[0])
x.append(p2[0])
x.append(15)
x.append(0)
y.append(0)
y.append(q1[0])
y.append(q2[0])
y.append(0)
y.append(10)

plt.fill_between(x, y, color = 'red', alpha = 0.6)

#Plotting the point of intersections
print("Intersection 1: ")
print(p1[0])
print(q1[0])
print("Intersection 2: ")
print(p2[0])
print(q2[0])

#Calculating values of Z function
z = []
for i in range(0,5):
    max_eqn = 40*x[i] + 80*y[i]
    z.append(max_eqn)
print("\nThe values of Z are: ", z)

#Showing plot
print()
plt.show()
print()

#Optimal Solution
maxval = max(z)
xy = z.index(maxval)
print(f"The maximum profit of Z (40x+80y) ={int(maxval)}, at point ({x[xy]},{y[xy]})")







