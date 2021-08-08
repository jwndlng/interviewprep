
from collections import deque

#
# Problem: https://www.youtube.com/watch?v=qz9tKlF431k
# Solution without kosaraju's algorithm
#


airports = [
    "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
    "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"
]

routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"],

]

# Global
last = None
L = deque()
visited = {airport:False for airport in airports}

# build adjaceny list and reverse adj list
adj = {}
adjR = {}
for ap in airports:
    adj[ap] = []
    adjR[ap] = []

for route in routes:
    adj[route[0]].append(route[1])
    adjR[route[1]].append(route[0])

def dfs(u):
    if visited[u]: return
    visited[u] = True
    for neighbor in adj[u]:
        dfs(neighbor)

def dfs_reverse(u):
    # Find root
    if visited[u]: return
    print(u)
    global last
    last = u
    visited[u] = True
    for neighbor in adjR[u]:
        dfs_reverse(neighbor)
        visited[neighbor] = False


def main():

    start = 'LGA'
    count = 0
    added_routes = []

    # Target: Find the missing links to make it possible that you
    # can fly from "LGA" to everywhere else

    # 1) Find nodes without an inbound edge and add them
    for airport in adjR:
        if len(adjR[airport]) == 0 and airport != start:
            count+=1
            adjR[airport].append(start)
            adj[start].append(airport)
            added_routes.append(f"{start} --> {airport}")


    # After adding the verteces with an indegree of 0 we check again
    # the reachability with a simple dfs
    dfs(start)

    # For all not visited vertices we find the root node and
    # add the connection
    for airport in visited:
        if visited[airport]: continue
        dfs_reverse(airport)
        dfs(last)
        count+=1
        adjR[airport].append(start)
        adj[start].append(last)
        added_routes.append(f"{start} --> {last}")
        

    # Measure Result
    print(f"Count of added routes {count}")
    print(f"Added routes:\n{added_routes}")

if __name__ == '__main__':
    main()


