"""
Source: https://www.youtube.com/watch?v=vHKzIPwWQkg

Problem:
Find the nodes that are not connected to the border and have a 1
if found replace them with 0. A valid border is a node on the edge
with a 1 as value

Solution for the problem below is:
array = [
    [1,0,0,0,0,0],
    [0,X,0,1,1,1],
    [0,0,X,0,1,0],
    [1,1,0,0,1,0],
    [1,0,X,X,0,0],
    [1,0,0,0,0,1]
]

"""


n=6
m=6

array = [
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [0,0,1,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,1,0,0],
    [1,0,0,0,0,1]
]

border_connection = [False for i in range(0, (n*m))]
visited = [False for i in range(0, (n*m))]


def is_valid_border(x, y):
    if (x == n-1 or y == m-1 or x == 0 or y == 0) and array[y][x] == 1:
        return True
    return False

def in_boundary(x, y):
    return (x < n and y < m and x >= 0 and y >= 0)

def has_border_connection(x, y):
    return border_connection[(n*y+x)]

def get_neighbors(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def dfs(x, y):
    # skip if not in boundaries!
    if not in_boundary(x, y): return
    # define node id
    node_id = (n*y+x)
    # check if visited!
    if visited[node_id]: return
    # if not visited, then visit!
    visited[node_id] = True
    # Return 0 valued cells
    if array[y][x] == 0: return

    if is_valid_border(x, y):
        border_connection[node_id] = True
        return

    for nx, ny in get_neighbors(x, y):
        dfs(nx, ny)
        if has_border_connection(nx, ny):
            border_connection[node_id] = True
            return
        
def is_connected(x, y):
    dfs(x,y)
    return (has_border_connection(x, y))


if __name__ == "__main__":

    import pprint

    pprint.pprint(array)

    for y in range(0, m-1):
        for x in range(0, n-1):
            if not is_connected(x, y) and array[y][x] == 1:
                print(f"Replace x:{x} y:{y} value {array[y][x]}")               
                array[y][x] = 'X'

    pprint.pprint(array)