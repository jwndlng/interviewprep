"""
 This is a sample implementation of Depth First Search (DFS)
 - For the graph we will be using an adjaceny list
 - We will just walk through a mark the nodes as visited
"""

import secrets

n = 13
visited = [False for i in range(0, n)]

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

def dfs(node_id):
    if visited[node_id]: return
    print(f"Visiting {node_id}")
    visited[node_id] = True
    print(visited)

    # get neighbors
    for id_ in adl[node_id]:
        dfs(id_)


def main():

    snode = secrets.randbelow(n+1)
    print(f"Starting DFS with Node {snode}")
    dfs(snode)


if __name__ == '__main__':
    main()