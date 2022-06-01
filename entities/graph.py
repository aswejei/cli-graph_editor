from entities.edge import Edge
from entities.node import Node
from exceptions.exceptions import TryingToAddExistingNodeException, TryingToDeleteUnexistingEdgeException, \
    TryingToDeleteUnexistingNodeException, TryingToSetNameForUnexistingNode, \
    TryingToAddEdgeWhichDoesntMatchGraphOrientation


class Graph:
    __name = 0
    __id = 0

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

    def AddNode(self, node: Node = None, name: str = '', color: str = 'white', shape: str = 'circle') -> None:
        if node is not None:
            if node not in self.__nodes_dict.values():
                self.__nodes_dict[node.id] = node
            else:
                raise TryingToAddExistingNodeException()
        else:
            add_node = Node(name=name, color=color, shape=shape)
            self.__nodes_dict[node.id] = add_node

    def AddEdge(self, node1: Node, node2: Node, color='white', orientation=False) -> None:
        if self.__orientation is orientation:
            e = Edge(node1, node2, color=color, orientation=orientation)
            self.__edges_list.append(e)
            node1.add_edge(e)
            node2.add_edge(e)
        else:
            raise TryingToAddEdgeWhichDoesntMatchGraphOrientation()

    def GetEdgesListString(self) -> str:
        return_value = ''
        for i in self.__edges_list:
            return_value += f'((Node: name : {i.connected_nodes[0].name}, id : {i.connected_nodes[0].id}, color: {i.connected_nodes[0].color}, shape: {i.connected_nodes[0].shape}) {i.orientation_string} (Node: name : {i.connected_nodes[1].name}, id : {i.connected_nodes[1].id}, color: {i.connected_nodes[1].color}, shape: {i.connected_nodes[1].shape})) : id - {i.id}, color - {i.color}\n '
        return return_value

    def DeleteNode(self, id: int):
        if id not in self.__nodes_dict.keys():
            raise TryingToDeleteUnexistingNodeException()
        else:
            for i in self.__nodes_dict[id].edge_dict:
                self.edges_list.remove(i)
            del self.__nodes_dict[id]

    def DeleteEdge(self, id: int = None, node1: Node = None, node2: Node = None, orientation=False):
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
                if i.connected_nodes is (node1, node2) and orientation is i.orientation:
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

    def GetMatrix(self):
        a = [[0 for i in range(len(self.__nodes_dict))] for i in range(len(self.__nodes_dict))]
        for i in range(len(a)):
            loclst = self.__nodes_dict[i].get_availiable_nodes_list()
            for j in range(len(a[i])):
                if i is j:
                    a[i][j] = 1
            else:
                if j in loclst:
                    a[i][j] = 1
        return a

    def GetGraphInfoString(self) -> str:
        a=f'Graph: id: {self.__id}, name: {self.__name}, orientation: {self.__orientation}'
        return a