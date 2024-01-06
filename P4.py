# Name and Roll Number
print("Name: Ritabrata Das\nRoll Number: 20CS8002\n")

# Taking the number of rows and columns as input
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
print()

# Inputting the cost matrix for transportation in row-order
cost_matrix = list()
for i in range(0, n):
    rem = list()
    for j in range(0, m):
        k = int(input(f"Enter the element arr[{i}][{j}]: "))
        rem.append(k)
    cost_matrix.append(rem)
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

# Initializing empty matrix for allocations and least cost calculation
allocations = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
rem = []

# Least Cost Method
while True:
    min_cost = float('inf')
    min_supplier, min_customer = None, None

    for i in range(n):
        for j in range(m):
            if cost_matrix[i][j] < min_cost and supply[i] > 0 and demand[j] > 0:
                # Calculating the minimum cost in matrix
                min_cost = cost_matrix[i][j]
                min_supplier, min_customer = i, j

    # Condition in case total supply and total demand equals zero
    if min_supplier is None or min_customer is None:
        break

    # Allocating the quantity and adding them to least cost
    allocation_quantity = min(supply[min_supplier], demand[min_customer])
    ans += min_cost*allocation_quantity

    # Storing thr allocation in a list
    rem.append(f"{min_cost}*{allocation_quantity}")

    # After allocation, modifying the latest demand and supply
    allocations[min_supplier][min_customer] = allocation_quantity
    supply[min_supplier] -= allocation_quantity
    demand[min_customer] -= allocation_quantity

# Printing the least cost and allocation order
print("The supply chain have the following order: ", rem)
print("The least cost of the transportation problem using LCM is: ", ans)
