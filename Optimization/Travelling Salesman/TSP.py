import sys

def tsp(graph, V):
    # Store all vertices except the starting vertex
    vertex = [i for i in range(V)]
    
    # Store minimum weight Hamiltonian Cycle
    min_path = sys.maxsize
    
    while True:
        # Store current path weight
        current_pathweight = 0
        
        # Compute current path weight
        k = 0
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        current_pathweight += graph[k][0]  # Return to the starting city
        
        # Update minimum
        min_path = min(min_path, current_pathweight)
        
        if not next_permutation(vertex):
            break
    
    return min_path

def next_permutation(L):
    n = len(L)
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = n - 1
    while L[j] <= L[i]:
        j -= 1
    L[i], L[j] = L[j], L[i]
    left = i + 1
    right = n - 1
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return True

# Example graph representation (adjacency matrix)
# graph = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

# graph= [[ 0, 2, 9, 100 ],
#         [ 1, 0, 6, 4 ],
#         [ 100, 7, 0, 8 ],
#         [ 6, 3, 100, 0 ]]

graph= [[ 0,10,15,20 ],
			[ 10,0 ,35,25 ],
			[ 15 ,35 , 0 ,30 ],
			[ 620 ,25 ,30 , 0 ]]
V = 4  # Number of vertices

# Find the minimum path
min_cost = tsp(graph, V)
print("Minimum Cost:", min_cost)
