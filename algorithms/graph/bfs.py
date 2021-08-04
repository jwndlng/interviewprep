"""
 This is a sample implementation of Breadth First Search (BFS)
 - For the graph we will be using an adjaceny list
 - We will just walk through a mark the nodes as visited
"""

import secrets
from queue import Queue

# Nodes in graph
n = 13

# adjaceny list
adl = {}
adl[0] = [1, 9]
adl[1] = [0, 8]
adl[2] = [3, 12]
adl[3] = [2, 4, 5, 7]
adl[4] = [3]
adl[5] = [3, 6]
adl[6] = [5, 7]
adl[7] = [3, 6, 8, 10, 11]
adl[8] = [1, 7, 9]
adl[9] = [0, 8]
adl[10] = [7, 11]
adl[11] = [7, 10]
adl[12] = [2]


def shortest_path(s, e):
    """
    The function will return the shortest path between two nodes
    """
    path = bfs(s)
    next = path[e]
    shortest_path = [e, next]

    while next != s:
        next = path[next]
        if next is None:
            return []
        shortest_path.append(next)
    shortest_path.reverse()
    return shortest_path 


def bfs(s):
    visited = [False for i in range(0, n)]
    path = [None for i in range(0, n)]
    q = Queue()
    q.put(s)
    visited[s] = True
    while not q.empty():
        next = q.get()
        for neighbor in adl[next]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path[neighbor] = next
                q.put(neighbor)
    return path


def main():
    print(f"Starting BFS with Node 0")
    path = shortest_path(0, 12)
    print(path)

if __name__ == "__main__":
    main()