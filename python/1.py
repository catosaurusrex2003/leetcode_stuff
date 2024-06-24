def getMinMaxLatency(g_nodes, g_from, g_to, g_weight, k):
    from collections import defaultdict
    import heapq

    # Check if there are no edges
    if not g_weight:
        # If the number of required components k is greater than or equal to the number of nodes
        # or if there are no nodes, return 0 since there are no connections
        return 0 if k >= g_nodes else float('inf')
    
    # Build the graph using an edge list where each entry is (weight, start, end)
    edges = [(w, start - 1, end - 1) for w, start, end in zip(g_weight, g_from, g_to)]
    
    # Sort edges based on their weights
    edges.sort()
    
    # Function to find the parent of a node in the Union-Find structure
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    # Function to union two sets in the Union-Find structure
    def union(parent, rank, x, y):
        rootX = find(parent, x)
        rootY = find(parent, y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
    
    def canFormKComponents(maxWeight):
        # Union-Find structure initialization
        parent = [i for i in range(g_nodes)]
        rank = [0] * g_nodes
        num_components = g_nodes
        
        # Only consider edges with weight <= maxWeight
        for weight, u, v in edges:
            if weight > maxWeight:
                break
            if find(parent, u) != find(parent, v):
                union(parent, rank, u, v)
                num_components -= 1
        
        return num_components <= k
    
    # Binary search over the edge weights
    low, high = 0, max(g_weight)
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        if canFormKComponents(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return answer
