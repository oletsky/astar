import math

#Illustrating A* algorithm
#Effectiveness can be improved by means of changing the heuristic function h

#Adjacent matrix representing the graph
#Key corresponds to the adjacent node and the value is a distance to it
graph = [
    {1: 1, 2: 10},
    {3: 100},
    {3: 5}
]
nodes = [0, 1, 2, 3]
h = [0, 0, 0, 0] # Heuristic function. Try to find a more informative one
start = 0
end = 3
distances = []
for v in range(len(nodes)):
    if (v == start):
        distances.append(0)
    else:
        distances.append(math.inf)
open = [start] # OPEN list
close = [] # CLOSE list
found = False
expanded = -1
while True:
    # Finding vertex for opening
    if len(open) == 0:
        # No ways
        break
    minim = math.inf

    #Finding a node to be expanded
    for v in open:
        if (distances[v] + h[v] < minim): # h is taken into account
            minim = distances[v] + h[v]
            expanded = v
    # Expanded node is end means that the Way is found
    if (expanded == end):
        found = True
        close.append(end)
        break
    # Expanding node
    open.remove(expanded)
    close.append(expanded)
    for v in graph[expanded].keys():
        if ((v not in open) and (v not in close)):
            open.append(v)
        if (distances[expanded] + graph[expanded][v] < distances[v]):
            distances[v] = distances[expanded] + graph[expanded][v]
if (found):
    print("The length of the shortest way is ", distances[end])
    print(close)
    print(len(close), " nodes have been expanded and got to CLOSE")
else:
    print("No ways found")



