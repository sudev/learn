from __future__ import annotations
import enum
from typing import List, Mapping
import sys

## Code more closer to CLRS, idiomatic python code with lesser frills given below.
class Colour(enum.Enum):
    WHITE = 1
    GREY = 2
    BLACK = 3

class Queue(object):
    def __init__(self):
        self.holder_list = []
    
    def push(self, val1):
        self.holder_list.append(val1)

    def pop(self):
        return self.holder_list.pop(0)

    def peek(self):
        return self.holder_list[0]

    def is_empty(self) -> bool:
        return len(self.holder_list) > 0

class Node(object):
    def __init__(self, value: str, colour: Colour,
                 connected_nodes: List[Node], distance = 0):
        self.value = value
        self.colour = colour
        self.connected_nodes = connected_nodes
        self.distance = distance
    def __str__(self):
        return "NODE :: value => {} colour => {} connected_nodes => {}".format(self.value,self.colour, self.connected_nodes)

class Graph(object):
    def __init__(self):
        self.graph: Mapping[str, Node] = {}

    def getOrCreate(self, v: str):
        if v in  self.graph:
            return self.graph[v]
        node = Node(v, Colour.WHITE, [])
        self.graph[v] = node
        return self.graph[v]
        

    def add_edge(self, u: str, v: str):
        (self.getOrCreate(u).connected_nodes).append(self.getOrCreate(v))
    
    def bfs(self, src: str):
        q = Queue()
        src_node = self.getOrCreate(src)
        print(src_node.value)
        [q.push(x) for x in src_node.connected_nodes]
        src_node.colour = Colour.BLACK
        while(q.is_empty()): 
            curNode: Node = q.pop()
            print(curNode)
            for adjNode in curNode.connected_nodes:
                adjNode.colour = Colour.GREY
                adjNode.distance = curNode.distance + 1
                q.push(adjNode)
            curNode.colour = Colour.BLACK

def driverWithFrills():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    graph.bfs(1)

# No frills code
queue = []
visited = []
def bfs(graph, visited, src_node):
    visited.append(src_node)
    queue.append(src_node)
    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    driverWithFrills()
    graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
    bfs(graph, visited, 'A')