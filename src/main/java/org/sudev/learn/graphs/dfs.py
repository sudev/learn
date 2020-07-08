graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
# A graph with loops
graph_clrs = {
    'u': ['v', 'x'],
    'v': ['y'],
    'y': ['x'],
    'x': ['v'],
    'w': ['y', 'z'],
    'z': ['z']
}
visited = {}


def dfs_util(graph, node):
    visited[node] = 1
    for child in graph[node]:
        if child in visited:
            continue
        dfs_util(graph, child)
    visited[node] = 2
    print(node)


# Given non-connected graph the dfs search depends on the starting node,
# sometimes you wont be able to reach to every given a starting node
def dfs(graph):
    for node in graph:
        if node not in visited:
            dfs_util(graph, node)


if __name__ == "__main__":
    dfs(graph_clrs)
    dfs(graph)
    # If it's a well connected graph the we can use the util function too.
    dfs_util(graph, 'A')