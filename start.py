import interface
from graph import Graph
from vertex import Vertex

def bulidGraph(g,VERS,edges):
    for c in range(VERS):
        g.addVertex(Vertex(c))
    for v in list(edges.keys()):
        edgs = edges[v].split("-")
        for e in edgs:
            edg = e.split(",")
            if(edg[0].isnumeric() and edg[1].isnumeric()):
                to = int(edg[0])
                w = int(edg[1])
                mainGraph.addEdge(v,to,w)
    return g

def getEdges(VERS):
    edges = {}
    print("Enter edges like this: 2,9-5,0\n2 edges sperated with -, each edge (to,w)")
    for v in range(VERS):
        user = ""
        print(f"============= Edges from {v} ============")
        user = input()
        edges[v] = user
    return edges

#VERS_PER_ROW = int(input("Enter the number of nodes per row: "))
VERS_PER_ROW = 5
VERS = VERS_PER_ROW*VERS_PER_ROW
mainGraph = Graph()

#edges = getEdges(VERS)
edges = {0: '1,5-6,3', 1: '2,15', 2: '3,2-7,3', 3: '4,1', 4: '9,3', 5: '', 6: '7,2-12,15', 7: '12,6', 8: '7,3', 9: '8,5-14,3', 10: '', 11: '', 12: '17,15', 13: '', 14: '', 15: '', 16: '', 17: '18,3', 18: '', 19: '', 20: '', 21: '', 22: '', 23: '', 24: ''}
print(edges)
mainGraph = bulidGraph(mainGraph,VERS,edges)

mainInterface = interface.Interface(mainGraph,VERS_PER_ROW)
mainInterface.main()