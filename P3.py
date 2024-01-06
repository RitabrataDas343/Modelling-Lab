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
total_supply, total_demand = 0, 0

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
else:
    print("It is a UNBALANCED problem.\n")

# Initializing the variables with the northwest corner
startR, startC, ans  = 0, 0, 0
rem = []

while(startR != n and startC != m):
    # Checking the position of North West Corner
    if(supply[startR] <= demand[startC]):
        # Updating the cost and modifying the allocations
        ans += supply[startR] * grid[startR][startC]
        rem.append(f"{supply[startR]}*{grid[startR][startC]}")
        demand[startC] -= supply[startR]
        startR += 1
    else:
        # Updating the cost and modifying the allocations
        ans += demand[startC] * grid[startR][startC]
        rem.append(f"{supply[startR]}*{grid[startR][startC]}")
        supply[startR] -= demand[startC]
        startC += 1

# Printing the NWCM cost and allocation order
print("The supply chain have the following order: ", rem)
print("The initial feasible basic solution using NWCM is: ", ans)
