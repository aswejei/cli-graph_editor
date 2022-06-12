import copy

from entities.edge import Edge
from entities.node import Node
from exceptions.exceptions import TryingToAddExistingNodeException, TryingToDeleteUnexistingEdgeException, \
    TryingToDeleteUnexistingNodeException, TryingToSetNameForUnexistingNode, \
    TryingToAddEdgeWhichDoesntMatchGraphOrientation, TryingToAddEdgeBetweenGraphs

import networkx as nx
from networkx.algorithms import tournament
from colorama import Fore


class Graph:
    __name = 0
    __id = 0
    colors_dict = {'red': Fore.RED, 'blue': Fore.BLUE, 'white': Fore.WHITE, 'yellow': Fore.YELLOW,
                   'green': Fore.GREEN, 'cyan': Fore.CYAN, 'magenta': Fore.MAGENTA}

    colors_dict_inverted = {Fore.RED: 'red', Fore.BLUE: 'blue', Fore.WHITE: 'white', Fore.YELLOW: 'yellow',
                            Fore.GREEN: 'green', Fore.CYAN: 'cyan', Fore.MAGENTA: 'magenta'}

    def __init__(self, name='', orientation=False):
        if name == '':
            self.__name = f'{Graph.__name}'
            Graph.__name += 1
        else:
            self.__name = name
        self.__id = Graph.__id
        Graph.__id += 1
        self.__orientation = orientation
        self.__nodes_dict = dict()
        self.__edges_list = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def edges_list(self) -> list:
        return self.__edges_list

    @property
    def nodes_dict(self) -> dict:
        return self.__nodes_dict

    @property
    def id(self) -> int:
        return self.__id

    def AddNode(self, name: str = '', color: str = 'white', shape: str = 'circle') -> str:
        if color == '': color = 'white'
        if shape == '': shape = 'circle'
        add_node = Node(name=name, color=color, shape=shape)
        self.__nodes_dict[add_node.id] = add_node
        return f'Node has been added: id - {add_node.id}, name - {add_node.name}, color - {add_node.color}, shape - {add_node.shape}\n'

    def AddEdge(self, node1: int, node2: int, color='white') -> None:
        if node1 not in self.__nodes_dict.keys() or node2 not in self.__nodes_dict.keys():
            raise TryingToAddEdgeBetweenGraphs()
        else:
            e = Edge(self.__nodes_dict[node1], self.__nodes_dict[node2], color=color, orientation=self.__orientation)
            self.__edges_list.append(e)
            self.__nodes_dict[node1].add_edge(e)
            self.__nodes_dict[node2].add_edge(e)
            return e.GetEdgeString()

    def __GetNodesListString(self) -> str:
        return_value = ''
        for i in self.__nodes_dict.values():
            return_value += Graph.colors_dict[
                                i.color] + f'Node: name : {i.name}, id : {i.id}, color: {i.color}, shape: {i.shape}\n'
        return return_value

    def __GetEdgesListString(self) -> str:
        return_value = ''
        for i in self.__edges_list:
            return_value += Graph.colors_dict[i.color] + '(' + Graph.colors_dict[i.connected_nodes[
                0].color] + f'(Node: name : {i.connected_nodes[0].name}, id : {i.connected_nodes[0].id}, color: {i.connected_nodes[0].color}, shape: {i.connected_nodes[0].shape})' + \
                            Graph.colors_dict[i.color] + f' {i.orientation_string}' + Graph.colors_dict[
                                i.connected_nodes[
                                    1].color] + f'(Node: name : {i.connected_nodes[1].name}, id : {i.connected_nodes[1].id}, color: {i.connected_nodes[1].color}, shape: {i.connected_nodes[1].shape})' + \
                            Graph.colors_dict[i.color] + f') : id - {i.id}, color - {i.color}\n '
        return return_value

    def DeleteNode(self, id: int):
        if id not in self.__nodes_dict.keys():
            raise TryingToDeleteUnexistingNodeException()
        else:
            for i in self.__nodes_dict[id].edge_dict.values():
                self.edges_list.remove(i)
            del self.__nodes_dict[id]

    def DeleteEdge(self, id: int = None, node1: Node = None, node2: Node = None):
        if id is not None:
            edge = None
            for i in self.__edges_list:
                if i.id is id:
                    edge = i
            for i in edge.connected_nodes:
                i.delete_edge(edge)
            self.__edges_list.remove(edge)
        elif node1 is not None and node2 is not None:
            edge = None
            for i in self.__edges_list:
                f = tuple(k.id for k in i.connected_nodes)
                k = (node1, node2)
                if f == k:
                    edge = i
                    break
            for i in edge.connected_nodes:
                i.delete_edge(edge)
            self.__edges_list.remove(edge)
        else:
            raise TryingToDeleteUnexistingEdgeException()

    def SetNodeName(self, node_id, name):
        if node_id in self.nodes_dict.keys():
            self.nodes_dict[node_id].name = name
        else:
            raise TryingToSetNameForUnexistingNode()

    def CheckIfNodesConnected(self, id1, id2):
        a = False
        if id1 == id2:
            a = True
        for i in self.__edges_list:
            if self.__orientation:
                if i == (id1, id2):
                    a = True
                    break
            else:
                if i == (id1, id2) or i == (id2, id1):
                    a = True
                    break
        return a

    def GetMatrix(self):
        a = {i: self.__nodes_dict[i].get_available_nodes_list() for i in self.__nodes_dict.keys()}
        return a

    def GetGraphInfoString(self) -> str:
        a = f'Graph: id: {self.__id}, name: {self.__name}, orientation: {self.__orientation}\n'
        if len(self.__nodes_dict) != 0:
            a += self.__GetNodesListString()
        if self.__edges_list:
            a += self.__GetEdgesListString()
        return a

    def GetAllNodeIDs(self):
        return list(self.__nodes_dict.keys())

    def GetAllEdgesIDs(self):
        k = [i.id for i in self.__edges_list]
        return k

    def __MakeIncedenceList(self):
        a = [[i.connected_nodes[0].id, i.connected_nodes[1].id] for i in self.__edges_list]
        return a

    def SetNodeColor(self, id, color):
        self.__nodes_dict[id].color = color

    def ConvertToNetworkxGraph(self):
        if self.__orientation:
            g = nx.MultiDiGraph()
            g.add_edges_from(self.__MakeIncedenceList())
        else:
            g = nx.MultiGraph()
            g.add_edges_from(self.__MakeIncedenceList())
        return g

    def IsConnected(self):
        g = self.ConvertToNetworkxGraph()
        a = nx.node_connectivity(g)
        if a == 0:
            return False
        else:
            return True

    def MakeConnected(self):
        g = self.ConvertToNetworkxGraph()
        s = nx.all_pairs_node_connectivity(g)
        for i in s.keys():
            for k in s[i].keys():
                if s[i][k] == 0:
                    self.AddEdge(i, k)

    def GetHamiltonianPath(self):
        g = self.ConvertToNetworkxGraph()
        p = tournament.hamiltonian_path(g)
        if not p:
            p = 'No hamiltonian path exist'
        return p

    def GetDiamRadCent(self):
        g = self.ConvertToNetworkxGraph()
        r = nx.radius(g)
        d = nx.diameter(g)
        c = list(nx.center(g))
        return d, r, c

    def ColorGraph(self):
        a = self.GetMatrix()
        colored = []
        colors = list(Graph.colors_dict.keys())
        for i in a.keys():
            local_colors = copy.copy(colors)
            for k in a[i]:
                z = self.__nodes_dict[k].color
                if z in local_colors:
                    local_colors.remove(z)
            if i not in colored:
                self.__nodes_dict[i].color = local_colors.pop()
                colored.append(i)
