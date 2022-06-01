class Node:
    __id = 0

    def __init__(self, name='', color='white', shape='circle'):
        self.__id = Node.__id
        Node.__id += 1
        self.__name = name
        self.__color = color
        self.__shape = shape
        self.__edge_dict = dict()

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
        self.__name=value

    def __hash__(self):
        return hash(self.__id)

    def add_edge(self, edge) -> None:
        self.__edge_dict[edge.id] = edge

    def del_edge(self, edge) -> None:
        del self.__edge_dict[edge.id]

    def get_availiable_nodes_list(self) -> list:
        lst=[]
        if list(self.__edge_dict.values())[0].orientation:
            for i in self.__edge_dict.values():
                lst.append(i.connected_nodes[1].id)
        else:
            for i in self.__edge_dict.values():
                    if i.connected_nodes[0]==self:
                        lst.append(i.connected_nodes[1].id)
                    else:
                        lst.append(i.connected_nodes[0].id)
        return lst