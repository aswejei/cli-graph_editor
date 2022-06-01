from entities.edge import Edge, Node
from entities.graph import Graph

n1=Node()
n2=Node()

a=Edge(n1, n2)

s=Graph()
s.AddNode(n1)
s.AddNode(n2)
s.AddEdge(s.nodes_dict[0], s.nodes_dict[1])
a=s.GetMatrix()
print(a)
print(s)



def i(a=5, **kwargs):
    print(a)
    print(kwargs)


