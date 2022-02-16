from vertex import Vertex
from edge import Edge
import queue
from queue import LifoQueue
class Graph:
    def __init__(self):
        self.__adj = {}

    def addVertex(self,vertex):
        vertices = list(self.__adj.keys())
        if isinstance(vertex,Vertex) and vertex.getName() not in vertices:
            self.__adj[vertex.getName()] = []
            return True
        return False
    
    def addEdge(self,From,To,W=0):
        vertices = list(self.__adj.keys())
        if From in vertices and To in vertices:
            newEdge = Edge(To,From,W)
            self.__adj[From].append(newEdge)
            return True
        return False
    def addEdgeUnd(self,v1,v2,w):
        self.addEdge(v1,v2,w)
        self.addEdge(v2,v1,w)
    def getAdj(self):
        vertices = list(self.__adj.keys())
        #for ver in vertices:
        #    print(f"{ver}:")
        #    for v in self.__adj[ver]:
        #        print("\t"+str(v.To()))
        return self.__adj

    def BFS(self,source):
        result = []
        vertices = list(self.__adj.keys())
        colors = ["W"] * len(vertices)
        per = [-1] * len(vertices)
        distances = [float("inf")] * len(vertices)
        Q = queue.Queue()
        colors[source] = "G"
        distances[source] = 0
        Q.put(source)
        while not Q.empty():
            u = Q.get()
            for edge in self.__adj[u]:
                v = edge.To()
                if(colors[v] == "W"):
                    colors[v] = "G"
                    distances[v] = distances[u] + 1
                    per[v] = u
                    Q.put(v)
                    result.append(v)
            colors[u] = "B"
        #print(colors)
        #print(per)
        #print(distances)
        return result
    
    def DFS_Sweep(self):
        vertices = list(self.__adj.keys())
        colors = ["W"] * len(vertices)
        per = [-1] * len(vertices)
        disTime = [None] * len(vertices)
        finTime = [None] * len(vertices)
        time = 0
        for u in vertices:
            if(colors[u] == "W"):
                time = self.DFS_Visit(u,colors,per,disTime,finTime,time)
        print(per)
        print(disTime)
        print(finTime)
    
    def DFS_Visit(self,vertex,colors,per,disTime,finTime,time):
        time+=1
        disTime[vertex] = time
        colors[vertex] = "G"
        for edge in self.__adj[vertex]:
            v = edge.To()
            if(colors[v] == "W"):
                per[v] = vertex
                time = self.DFS_Visit(v,colors,per,disTime,finTime,time)
        colors[vertex] = "B"
        time+=1
        finTime[vertex] = time
        return time
    def relax(self,u,v,w,dis,Q,per):
        if(dis[v] > dis[u]+w):
            dis[v] = dis[u]+w
            Q[v] = dis[v]
            per[v] = u
    def sssp(self,source):
        vertices = list(self.__adj.keys())
        per = [-1] * len(vertices)
        distances = [float("inf")] * len(vertices)
        distances[source] = 0
        Q = [float("inf")] * len(vertices)
        Q[source] = 0
        c=0
        while c < len(vertices):
            u = Q.index(min(Q))
            Q[u] = float("inf")
            c+=1
            for edge in self.__adj[u]:
                v = edge.To()
                w = edge.W()
                self.relax(u,v,w,distances,Q,per)
        result = [[None],[None]]
        #print(distances)
        #print(per)
        result[0] = distances
        result[1] = per
        return result
    def getShortestPath(self,source,dest):
        can = self.BFS(source)
        if dest not in can:
            return
        final_res = [None,None,None]
        result = LifoQueue()
        all = self.sssp(source)
        distances = all[0]
        per = all[1]
        v = distances[dest]
        ver = dest
        while(v > 0):
            u = ver
            result.put(u)
            v = distances[per[u]]
            ver = per[u]
        result.put(source)
        temp = []
        while(not result.empty()):
            #print(result.get(), end=" -> ")
            temp.append(result.get())
        final_res[0] = temp
        temp = []
        temp.append(0)
        for i in range(len(final_res[0])-1):
            ver = final_res[0][i]
            for u in self.__adj[ver]:
                if (u.To() == final_res[0][i+1]):
                    temp.append(u.W())
                else:
                    continue
        final_res[1] = temp
        final_res[2] = distances[dest]
        return final_res