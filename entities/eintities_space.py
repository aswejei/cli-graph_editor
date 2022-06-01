from entities.graph import Graph
import copy


class NameSpace:
    def __init__(self):
        self.__graph_dict=dict()
        self.__current_graph=None

    def AddGraph(self, name='', orientation=False):
        s=Graph(name=name, orientation=orientation)
        self.__current_graph=s

    def SaveCurrentGraph(self):
        self.__graph_dict[self.__current_graph.id]=copy.deepcopy(self.__current_graph)

    def LoadGraph(self, id=-1):
        if id>-1:
            self.__current_graph=self.__graph_dict[id]

    def DeleteSavedGraph(self, id):
        del self.__graph_dict[id]

    def DeleteCurrentGraph(self):
        self.__current_graph=None

    def PrintCurrentGraph(self):
        print(self.__current_graph.GetEdgesListString())

    def PrintSavedGraphs(self):
        pass