import math
graph=[
        {1:1, 2:4,3:8},
        {4:2},
        {1:1,3:2,5:20},
        {5:1,6:50},
        {5:15,7:100},
        {6:2,7:50},
        {7:3}
    ]
nodes=[0,1,2,3,4,5,6,7]
start=0
end=7
distances=[]
for v in range(len(nodes)):
    if (v==start):
        distances.append(0)
    else:
        distances.append(math.inf)
open=[start]
close=[]
found=False
vtoexpand=-1
while True:
    #Finding vertex for opening
    if len(open)==0:
        #No ways
        break
    minim=math.inf
    for v in open:
        if (distances[v]<minim):
            minim=distances[v]
            vtoexpand=v
    #Way found
    if (vtoexpand==end):
        found=True
        close.append(end)
        break
    #Opening vertex
    open.remove(vtoexpand)
    close.append(vtoexpand)
    for v in graph[vtoexpand].keys():
        if ((v not in open) and (v not in close)):
            open.append(v)
        if (distances[vtoexpand]+graph[vtoexpand][v]<distances[v]):
            distances[v]=distances[vtoexpand]+graph[vtoexpand][v]
if (found):
    print("The length of the shortest way is ",distances[end])
    print(close)
    print(len(close)," vertexes have been expanded and got to close")
else:
    print("No ways found")

