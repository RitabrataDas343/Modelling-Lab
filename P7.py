import numpy as np

class Transportation_Problem:
    def __init__(self,C,S,D):
        self.C = np.array(C).astype(float) # cost matrix
        self.S = np.array(S).astype(float) # supply matrix
        self.D = np.array(D).astype(float) # demand matrix
        self.A = np.zeros(self.C.shape).astype(float) # allocation matrix
        self.total_cost = 0
        self.no_alloc = 0
        self.total_demand = 0
        self.total_supply = 0
        self.rows,self.cols = self.C.shape
        self.u,self.v,self.delta = None,None,None
        
    def is_balanced(self):
        self.total_demand = np.sum(self.D)
        self.total_supply = np.sum(self.S)
        return self.total_demand == self.total_supply

    def make_balanced(self):
        if self.total_demand<self.total_supply:
            self.D = np.append(self.D,np.array([self.total_supply-self.total_demand])) 
            self.C = np.append(self.C,np.zeros((self.rows,1)),axis=1)
            self.total_demand = np.sum(self.D)
            self.rows,self.cols = self.C.shape
        elif self.total_demand>self.total_supply:
            self.S = np.append(self.S,np.array([self.total_demand-self.total_supply]))
            self.C = np.append(self.C,np.zeros((1,self.cols)),axis=0)
            self.total_supply = np.sum(self.S)
            self.rows,self.cols = self.C.shape
    
    def is_degenerate(self):
        return (self.rows+self.cols-1) == self.no_alloc
    
    def make_non_degenerate(self,d = 0.001):

        def is_independent(A):
            # eliminate rows and cols
            r,c = A.shape
            rows = list(range(r))
            cols = list(range(c))
            flag = True
            while flag:
                flag = False
                for r in rows[:]:
                    if np.count_nonzero(A[r,cols])<2:
                        rows.remove(r)
                        flag = True
                for c in cols[:]:
                    if np.count_nonzero(A[rows,c])<2:
                        cols.remove(c)
                        flag = True
            return not(len(rows)>0 and len(cols)>0)
            
                    
                
        diff = (self.rows+self.cols-1) - self.no_alloc
        empty_cells = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.A[r][c]==0:
                    empty_cells.append((self.C[r][c],r,c))
        empty_cells.sort()
        for i in range(diff):
            while empty_cells:
                _,r,c = empty_cells[0]
                empty_cells.pop(0)
                A = self.A.copy()
                A[r,c] = d
                if is_independent(A):
                    self.A[r,c] = d
                    break
            else:
                print("Warning : couldn't fix degeneracy")
    
    def recalculate_cost(self):
        self.total_cost = 0
        for i in range(self.rows):
            for j in range(self.cols):
                self.total_cost += self.C[i,j]*self.A[i,j]
    
    def input_cost(self):
        total_cost, no_alloc = 0, 0
        self.A = np.zeros(self.C.shape).astype(float)

        for i in range(self.A.shape[0]):
            for j in range(self.A.shape[1]):
                input_value = float(input(f"Enter the allocation for arr[{i}][{j}]: "))
                self.A[i][j] = input_value
                if(float(input_value) != 0):
                    total_cost += self.A[i][j] * self.C[i][j]
                    no_alloc += 1
        self.total_cost = total_cost
        self.no_alloc = no_alloc
        
    def is_optimal(self):
        max_row_alloc_count, row = max([(np.count_nonzero(self.A[r,:]),r) for r in range(self.rows)])
        max_col_alloc_count, col = max([(np.count_nonzero(self.A[:,c]),c) for c in range(self.cols)])
        u = np.zeros((self.rows))
        v = np.zeros((self.cols))

        if max_row_alloc_count<max_col_alloc_count:
            s = ('v',col)
            v[col] = 0
            print(f"Substituting v{col}=0, we get,")
        else:
            s = ('u',row)
            u[row] = 0
            print(f"Substituting u{row}=0, we get,")

        # bfs    
        visited = set()
        q = [s]
        while q:
            flag,index = q[0]
            if q[0] not in visited:
                if flag == 'u':
                    for i,a in enumerate(self.A[index,:]):
                        if a!=0:
                            v[i] = self.C[index][i]-u[index]
                            if ('v',i) not in visited:
                                print(f"u{index} = {u[index]} --> v{i} = {v[i]},")
                            q.append(('v',i))
                else:
                    for i,a in enumerate(self.A[:,index]):
                        if a!=0:
                            u[i] = self.C[i][index]-v[index]
                            if ('u',i) not in visited:
                                print(f"v{index} = {v[index]} --> u{i} = {u[i]},")
                            q.append(('u',i))

            visited.add(q[0])            
            q.pop(0)

        print("u = ",u,"\nv = ",v)
        
        delta = np.zeros((self.rows,self.cols))
        for i in range(self.rows):
            for j in range(self.cols):
                delta[i][j] = self.C[i][j]-u[i]-v[j]
        
        self.u,self.v,self.delta = u,v,delta
        print("Allocation of Delta :\n",delta)
        return not(np.any(delta<0))
    
    def modi(self):
        # give min delta a value
        min_del_i, min_del_j = np.unravel_index(np.argmin(self.delta, axis=None), self.delta.shape) 
        A = self.A.copy()
        A[min_del_i,min_del_j] = 0.00001
        
        # eliminate rows and cols
        rows = list(range(self.rows))
        cols = list(range(self.cols))
        flag = True
        while flag:
            flag = False
            for r in rows[:]:
                if np.count_nonzero(A[r,cols])<2:
                    rows.remove(r)
                    flag = True
            for c in cols[:]:
                if np.count_nonzero(A[rows,c])<2:
                    cols.remove(c)
                    flag = True
        
        # find all valid allocations for creating path
        allocs = []
        for r in rows:
            for c in cols:
                if A[r,c]!=0:
                    allocs.append((r,c))
                    
        # find the closed path
        path = [(min_del_i, min_del_j)]
        if (min_del_i, min_del_j) in allocs:
            allocs.remove((min_del_i, min_del_j))
        while allocs:
            last_i,last_j = path[-1]
            min_i,min_j = np.inf,np.inf
            for i,j in allocs:
                if i==last_i and abs(j-last_j)<abs(min_j-last_j):
                    min_i,min_j = i,j
                elif j==last_j and abs(i-last_i)<abs(min_i-last_i):
                    min_i,min_j = i,j
            path.append((min_i,min_j))
            allocs.remove((min_i,min_j))
        print("Closed path: "," -> ".join([f"S{i+1}D{j+1}" for i,j in path]))
        # find minimum at negetive position
        negs = [self.A[path[i][0],path[i][1]] for i in range(1,len(path),2)]
        min_neg = min(negs)
        for i in range(len(path)):
            if i%2==0:
                self.A[path[i][0],path[i][1]] += min_neg
            else:
                self.A[path[i][0],path[i][1]] -= min_neg
        self.no_alloc = np.count_nonzero(self.A!=0)
        
        
            
    def solve(self,initial_sol_func):
        if self.is_balanced():
            print("It is a BALANCED problem.\n")
        else:
            print("It is a UNBALANCED problem.\n")
        # Converting to Balanced Problem
        total_supply = np.sum(self.S)
        total_demand = np.sum(self.D)
        s,d = self.C.shape
        if(total_supply > total_demand):
            for row in C:
                row.append(0)
            D.append(total_supply-total_demand)
            d += 1
        else:
            row = [0] * d
            C.append(row)
            S.append(total_demand-total_supply)
            s +=1

        initial_sol_func()
        print("Initial basic feasible solution:")
        print("Total Cost: ",self.total_cost)
        print("No of Allocation: ",self.no_alloc)
        print()
        print("Allocations:\n",self.A)
        if self.is_degenerate() and self.is_balanced():
            print("\nIt is not a Degenerate Solution")
        else:
            print("\nDegenerate Solution")
            print("\nAllotting dummy allocations ... ")
            tp.make_non_degenerate()
            print("\nNew Allocations:\n",tp.A)
        print()
        print("Checking optimality:")
        while not tp.is_optimal():
            print("\nThe given allocations are not optimal.")
            print("Applying MODI optimization: ")
            tp.modi()
            if self.is_degenerate() and self.is_balanced():
                print("It is not a Degenerate Solution")
            else:
                print("Degenerate Solution")
                print("allotting dummy allocations ... ")
                tp.make_non_degenerate()

            print("\nNew Allocations:\n",tp.A)
            tp.recalculate_cost()
            print("Total cost: ",tp.total_cost)
            print()
            print("Checking optimality:")
        print("\nThe allocations are optimal.")
        print()
        print("Final allocations:\n",tp.A)
        print("\nFinal minimimum cost:",tp.total_cost)
    
    
if __name__ == "__main__":
    np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
    print("Name: Ritabrata Das\nRoll Number: 20CS8002\n")
    s = int(input("Enter the number of rows: "))
    d = int(input("Enter the number of columns: "))
    print()

    C = list()
    for i in range(0, s):
        rem = list()
        for j in range(0, d):
            k = int(input(f"Enter the element arr[{i}][{j}]: "))
            rem.append(k)
        C.append(rem)
    print()

    S = list()
    for i in range(0, s):
        k = int(input(f"Enter the supply for Row {i+1}: "))
        S.append(k)
    print()

    D = list()
    for i in range(0, d):
        k = int(input(f"Enter the demand for Column {i+1}: "))
        D.append(k)
    print()

    tp = Transportation_Problem(C,S,D)
    tp.solve(initial_sol_func = tp.input_cost)