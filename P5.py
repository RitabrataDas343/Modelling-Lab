# Function for calculating the row penalties and the column penalties
def calculatePenalties(grid):
	rowDiff = []
	colDiff = []
	for i in range(len(grid)):
		arr = grid[i][:]
		arr.sort()
		rowDiff.append(arr[1]-arr[0])
	col = 0
	while col < len(grid[0]):
		arr = []
		for i in range(len(grid)):
			arr.append(grid[i][col])
		arr.sort()
		col += 1
		colDiff.append(arr[1]-arr[0])
	return rowDiff, colDiff

def vogel_approximation(grid, supply, demand, n, m, ans):
    # Loop runs until both the demand and the supply is exhausted
    rem = []
    while max(supply) != 0 or max(demand) != 0:
        # Finding the row and column penalties
        row, col = calculatePenalties(grid)
        # Finding the maxiumum element in row penalties array
        maxi1 = max(row)
        # Finding the maxiumum element in col penalties array
        maxi2 = max(col)

        # If the row difference max element is greater than or equal to column difference max element
        if(maxi1 >= maxi2):
            for ind, val in enumerate(row):
                if(val == maxi1):
                    # Finding the minimum element in grid index where the maximum was found in the row difference
                    mini1 = min(grid[ind])
                    for ind2, val2 in enumerate(grid[ind]):
                        if(val2 == mini1):
                            # Calculating the min of supply and demand in that row and col
                            mini2 = min(supply[ind], demand[ind2])
                            ans += mini2 * mini1
                            rem.append(f"{mini2}*{mini1}")
                            # Subtracting the min from the supply and demand
                            supply[ind] -= mini2
                            demand[ind2] -= mini2
                            # If demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
                            if(demand[ind2] == 0):
                                for r in range(n):
                                    grid[r][ind2] = INF
                            # If supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
                            else:
                                grid[ind] = [INF for i in range(m)]
                            break
                    break
        # If the row diff max element is greater than col diff max element
        else:
            for ind, val in enumerate(col):
                if(val == maxi2):
                    # Finding the minimum element in grid index where the maximum was found in the col difference
                    mini1 = INF
                    for j in range(n):
                        mini1 = min(mini1, grid[j][ind])

                    for ind2 in range(n):
                        val2 = grid[ind2][ind]
                        if val2 == mini1:
                            # Calculating the min of supply and demand in that row and col
                            mini2 = min(supply[ind2], demand[ind])
                            ans += mini2 * mini1
                            rem.append(f"{mini2}*{mini1}")
                            # Subtracting the min from the supply and demand
                            supply[ind2] -= mini2
                            demand[ind] -= mini2
                            # If demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
                            if(demand[ind] == 0):
                                for r in range(n):
                                    grid[r][ind] = INF
                            # If supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
                            else:
                                grid[ind2] = [INF for i in range(m)]
                            break
                    break
    print("The supply chain have the following order: ", rem)
    print("The basic feasible solution is: ", ans)

# Name and Roll Number
print("Name: Ritabrata Das\nRoll Number: 20CS8002\n")

# Taking the number of rows and columns as input
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
print()

# Inputting the cost matrix for transportation in row-order
grid = list()
for i in range(0, n):
    rem = list()
    for j in range(0, m):
        k = int(input(f"Enter the element arr[{i}][{j}]: "))
        rem.append(k)
    grid.append(rem)
print()

# Initializing variables to calculate total supply and demand
total_supply, total_demand, ans = 0, 0, 0
INF = 10**3

# Taking the supply for each row and calculating total supply
supply = list()
for i in range(0, n):
    k = int(input(f"Enter the supply for Row {i+1}: "))
    supply.append(k)
    total_supply += k
print()

# Taking the demand for each column and calculating total demand
demand = list()
for i in range(0, m):
    k = int(input(f"Enter the demand for Column {i+1}: "))
    demand.append(k)
    total_demand += k
print()

# Checking if it is a balanced problem or not
if(total_demand == total_supply):
    print("It is a BALANCED problem.\n")
    vogel_approximation(grid, supply, demand, n, m, ans)
else:
    print("It is a UNBALANCED problem.\n")
    # Converting to Balanced Problem
    if(total_supply > total_demand):
        for row in grid:
            row.append(0)
        demand.append(total_supply-total_demand)
        vogel_approximation(grid, supply, demand, n, m+1, ans)
    else:
        row = [0] * m
        grid.append(row)
        supply.append(total_demand-total_supply)
        vogel_approximation(grid, supply, demand,  n+1, m, ans)