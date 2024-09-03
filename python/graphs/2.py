def create_adjacency_list(edges, num_vertices):
    # Initialize the adjacency list
    adj_list = [[] for _ in range(num_vertices)]

    # Fill the adjacency list based on the edges in the graph
    for u, v in edges:
        # Since the graph is undirected, push the edges in both directions
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list

if __name__ == "__main__":
    # Undirected Graph of 4 nodes
    num_vertices = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 1)]

    # Create the adjacency list
    adj_list = create_adjacency_list(edges, num_vertices)

    # Print the adjacency list
    for i in range(num_vertices):
        print(f"{i} -> {' '.join(map(str, adj_list[i]))}")
