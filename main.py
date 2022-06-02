from entities.edge import Edge, Node
from entities.eintities_space import GraphSpace
from entities.graph import Graph

# n1=Node()
# n2=Node()
#
# a=Edge(n1, n2)
#
# s=Graph(orientation=True)
# s.AddNode(n1)
# s.AddNode(n2)
# s.AddEdge(s.nodes_dict[0], s.nodes_dict[1], orientation=True)
# a=s.GetMatrix()
# print(s.GetGraphInfoString())
# s.SetNodeName(0, 'abc')
# print(s.GetGraphInfoString())
# s.DeleteNode(0)
# print(s.GetGraphInfoString())
from front.cli import CLI
#1
# import matplotlib
# import networkx as nx
# from networkx.algorithms import tournament
#
# g=nx.DiGraph()
# g.add_edges_from([[0,1],[2,3]])
# nx.draw(g)
# print(tournament.hamiltonian_path(g))

CLI.init()
CLI.main_menu()
import colorama
# from colorama import Fore
# print(Fore.RED +'aaa'+ Fore.BLUE+'vvv')
# gs = GraphSpace()
# gs.AddGraph(name='a', orientation=False)
# gs.SetCurrentGraph(0)

# gs.current_graph.AddNode()
# gs.current_graph.AddNode()
# gs.current_graph.AddEdge(0, 1)
# print(gs.GetCurrentGraphInfo())
# gs.SaveCurrentGraph()
# gs.current_graph.AddNode()
# gs.current_graph.AddEdge(0,2)
# print(gs.GetCurrentGraphInfo())
# gs.SaveCurrentGraph()
# print(gs.GetCurrentGraphInfo())
# gs.LoadSavedGraph(graph_id=0, saving_id=0)
# print(gs.GetCurrentGraphInfo())
# gs.LoadSavedGraph(graph_id=0, saving_id=2)
# print(gs.GetCurrentGraphInfo())
# gs.LoadSavedGraph(graph_id=0, saving_id=1)
# print(gs.GetCurrentGraphInfo())

def i(a=5, **kwargs):
    print(a)
    print(kwargs)
