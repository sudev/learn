from __future__ import annotations
from typing import List, Mapping

professor_graph = {
    'undershorts': ['pants', 'shoes'],
    'pants': ['shoes', 'belt'],
    'belt': ['jacket'],
    'socks': ['shoes'],
    'watch': [],
    'shirt': ['tie', 'belt'],
    'tie': ['jacket'],
    'jacket': [],
    'shoes' :[]
}
class GNode(object):
    def __init__(self, data, start_time, end_time):
        self.data = data
        self.start_time = start_time
        self.end_time = end_time

sorted_nodes = []
# 0 = White, not-visited, 1 = GREY, 2 = BLACK
visited: Mapping[str, int] = {}
time = 0
def dfs_util(graph, graph_node, time):
    global sorted_nodes
    time = time + 1
    visited[graph_node] = 1
    for child in graph[graph_node]:
        if child in visited:
            continue
        dfs_util(graph, child, time)
    visited[graph_node] = 2
    # return final node, this will be the root for the given DFS - tree
    sorted_nodes = [graph_node] + sorted_nodes
    print("{} - {} ".format(time, graph_node))

for gnode in professor_graph:
    if gnode in visited:
        continue
    dfs_util(professor_graph, gnode, time)
    #sorted_nodes = []
