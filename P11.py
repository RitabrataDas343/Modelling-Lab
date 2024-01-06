import elkai

n = int(input("Enter the number of nodes: "))

number_to_letter = {}
for number in range(n):
    letter = chr(ord('A') + number)
    number_to_letter[number] = letter

dist = list()
for i in range(0, n):
    rem = list()
    for j in range(0, n):
        k = int(input(f"Enter the element arr[{i}][{j}]: "))
        rem.append(k)
    dist.append(rem)
print()

cities = elkai.DistanceMatrix(dist)

path = cities.solve_tsp()

path_as_str = ""
for i in path:
    path_as_str = path_as_str + number_to_letter[i] + "->"

print(f"The salesman travel from: {path_as_str[:-2]}")

tot = 0
for i in range(len(path)):
    if(i > 0):
        tot = tot + dist[path[i-1]][path[i]]

print("The total cost of the journey is:", tot)
