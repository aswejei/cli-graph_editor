from entities.node import Node
from colorama import Fore


class Edge:
    __id = 0
    __colors_dict = {'red': Fore.RED, 'blue': Fore.BLUE, 'white': Fore.WHITE, 'yellow': Fore.YELLOW,
                     'green': Fore.GREEN, 'cyan': Fore.CYAN}

    def __init__(self, node1: Node, node2: Node, color='white', orientation=False):
        self.__id = Edge.__id
        Edge.__id += 1
        self.__connected_nodes = (node1, node2)
        self.__orientation = orientation
        self.__color = color

    @property
    def id(self):
        return self.__id

    @property
    def color(self):
        return self.__color

    @property
    def connected_nodes(self):
        return self.__connected_nodes

    @property
    def orientation(self):
        return self.__orientation

    @property
    def orientation_string(self):
        if self.__orientation:
            return '=>'
        else:
            return '=='

    def GetEdgeString(self):
        return Edge.__colors_dict[
                   self.__color] + f'Edge: id - {self.__id}, color - {self.__color}, first node id - {self.__connected_nodes[0].id}, second node id - {self.__connected_nodes[1].id}\n'

    def IsOrientated(self):
        return self.__orientation

    def __eq__(self, other: tuple):
        k = False
        if self.__connected_nodes[0].id == other[0] and self.__connected_nodes[1] == other[1]:
            k = True
        return k

    def __hash__(self):
        return hash(self.__connected_nodes)
