def findDiff(grid):
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

def vogel_approximation_recursive(grid, supply, demand, n, m, rem, ans):

    if max(supply) == 0 or max(demand) == 0:
        print("The supply chain have the following order: ", rem)
        print("The basic feasible solution is: ", ans)
        return
    
    row, col = findDiff(grid)
    maxi1 = max(row)
    maxi2 = max(col)

    if maxi1 >= maxi2:
        for ind, val in enumerate(row):
            if val == maxi1:
                mini1 = min(grid[ind])
                for ind2, val2 in enumerate(grid[ind]):
                    if val2 == mini1:
                        mini2 = min(supply[ind], demand[ind2])
                        ans += mini2 * mini1
                        rem.append(f"{mini2}*{mini1}")
                        supply[ind] -= mini2
                        demand[ind2] -= mini2
                        if demand[ind2] == 0:
                            for r in range(n):
                                grid[r][ind2] = INF
                        else:
                            grid[ind] = [INF]*m
                        break
                break
    else:
        for ind, val in enumerate(col):
            if val == maxi2:
                mini1 = INF
                for j in range(n):
                    mini1 = min(mini1, grid[j][ind])

                for ind2 in range(n):
                    val2 = grid[ind2][ind]
                    if val2 == mini1:
                        mini2 = min(supply[ind2], demand[ind])
                        ans += mini2 * mini1
                        rem.append(f"{mini2}*{mini1}")
                        supply[ind2] -= mini2
                        demand[ind] -= mini2
                        if demand[ind] == 0:
                            for r in range(n):
                                grid[r][ind] = INF
                        else:
                            grid[ind2] = [INF] * m
                        break
                break
    vogel_approximation_recursive(grid, supply, demand, n, m, rem, ans)

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

grid = []
for i in range(n):
    rem = list()
    for j in range(m):
        tot = int(input(f"Enter the element grid[{i}][{j}]: "))
        rem.append(tot)
    grid.append(rem)
print()

total_supply, total_demand, ans = 0, 0, 0
INF = 10**6
supply = list()
demand = list()
rem = []

for i in range(n):
    tot = int(input(f"Enter the supply for Row No. {i+1}: "))
    supply.append(tot)
    total_supply += tot


for i in range(m):
    tot = int(input(f"Enter the demand for Column No. {i+1}: "))
    demand.append(tot)
    total_demand += tot

if(total_demand == total_supply):
    print("It is a Balanced problem.\n")
    vogel_approximation_recursive(grid, supply, demand, n, m, rem, ans)
else:
    print("It is a Unbalanced problem.\n")
    diff = abs(total_demand-total_supply)
    if(total_supply > total_demand):
        demand.append(diff)
        for row in grid:
            row.append(0)

        vogel_approximation_recursive(grid, supply, demand, n, m+1, rem, ans)
    else:
        supply.append(diff)
        row = [0] * m
        grid.append(row)
        
        vogel_approximation_recursive(grid, supply, demand, n+1, m, rem, ans)