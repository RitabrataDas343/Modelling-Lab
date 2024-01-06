# Name and Roll Number
print("Name: Ritabrata Das\nRoll Number: 20CS8002\n")

# n = int(input("Enter the number of nodes: "))

# dist = list()
# for i in range(0, n):
#     rem = list()
#     for j in range(0, n):
#         k = int(input(f"Enter the element arr[{i}][{j}]: "))
#         rem.append(k)
#     dist.append(rem)
# print()

# n = 4
ans = 10**9
# dist = [[ans, 4, 9, 5], [6, ans, 4, 8], [9, 4, ans, 9], [5, 8, 9, ans]]

n = 5
dist = [[ans,2,5,7,1],[6,ans,3,8,2],[8,7,ans,4,7],[12,4,6,ans,5],[1,3,8,2,ans]]

memo = [[-1]*(1 << (n+1)) for _ in range(n)]


def fun(i, mask):
	if mask == ((1 << i) | 3):
		return dist[1][i]

	if memo[i][mask] != -1:
		return memo[i][mask]

	res = 10**9 
	for j in range(1, n):
		if (mask & (1 << j)) != 0 and j != i and j != 1:
			res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
	memo[i][mask] = res 
	return res


for i in range(1, n):
	ans = min(ans, fun(i, (1 << (n))-1) + dist[i][1])

print("The cost of most efficient tour = " + str(ans))

