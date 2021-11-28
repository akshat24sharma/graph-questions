from queue import Queue
adj_list={
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}
visited={}
level={}
parent={}
bfs=[]
queue=Queue()

for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
    
s="A"
visited[s]=True
level[s]=0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs.append(u)
    
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(v)
print(bfs)

g="F"
path=[]
while g is not None:
    path.append(g)
    g=parent[g]
path.reverse()
print(path)
print(parent)