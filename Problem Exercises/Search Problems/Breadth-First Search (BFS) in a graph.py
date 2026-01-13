#Breadth-First Search (BFS) in a graph
from collections import deque
def bfs(graph,start):
    visited=set([start])
    q=deque([start])
    while q:
        node=q.popleft()
        print(node,end=" ")
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                q.append(neigh)

graph={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
bfs(graph,'A')  # A B C D E
