from exceptions.exceptions import TryingToAddExistingColor
from colorama import Fore

class Node:
    __id = 0
    __colors_dict = {'red': Fore.RED, 'blue': Fore.BLUE, 'white': Fore.WHITE, 'yellow': Fore.YELLOW,
                     'green': Fore.GREEN, 'cyan': Fore.CYAN, 'magenta' : Fore.MAGENTA}

    def __init__(self, name='', color='white', shape='circle'):
        self.__id = Node.__id
        Node.__id += 1
        self.__name = name
        self.__color = color
        self.__shape = shape
        self.__edge_dict = dict()
        self.__content=None

    @property
    def id(self):
        return self.__id

    @property
    def color(self):
        return self.__color

    @property
    def shape(self):
        return self.__shape

    @property
    def edge_dict(self):
        return self.__edge_dict

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @color.setter
    def color(self, value):
        self.__color = value

    def __hash__(self):
        return hash(self.__id)

    def add_edge(self, edge) -> None:
        self.__edge_dict[edge.id] = edge

    def delete_edge(self, edge) -> None:
        del self.__edge_dict[edge.id]

    def get_available_nodes_list(self) -> list:
        lst = []
        if list(self.__edge_dict.values())[0].orientation:
            for i in self.__edge_dict.values():
                lst.append(i.connected_nodes[1].id)
        else:
            for i in self.__edge_dict.values():
                if i.connected_nodes[0].id == self.__id:
                    lst.append(i.connected_nodes[1].id)
                else:
                    lst.append(i.connected_nodes[0].id)
        return lst

    def __str__(self):
        return f'Node: id - {self.__id}, name - {self.__name}, color - {self.__color}, shape - {self.__shape}'

    def __repr__(self):
        return f'Node: id - {self.__id}, name - {self.__name}, color - {self.__color}, shape - {self.__shape}'