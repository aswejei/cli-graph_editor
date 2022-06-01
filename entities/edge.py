from entities.node import Node


class Edge:
    __id = 0

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
    def orienation_string(self):
        if self.__orientation:
            return '=>'
        else:
            return '=='

    def IsOrientated(self):
        return self.__orientation

    def __hash__(self):
        return hash(self.__connected_nodes)
