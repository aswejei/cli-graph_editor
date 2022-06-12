import networkx as nx

from entities.graph import Graph
import copy

from exceptions.exceptions import TryingToLoadNonexistingSaving, TryingToDeleteNonexistingSaving, \
    TryingToDeleteNonSavedGraph, TryingToDeleteNonLoadedGraph, NoGraphLoadedToDelete, TryingToLoadNonexistingGraph


class GraphSpace:
    def __init__(self):
        self.__graph_dict = dict()
        self.__saved_graph_dict = dict()
        self.current_graph = None

    def AddGraph(self, name: str = '', orientation: bool = False) -> None:
        s = Graph(name=name, orientation=orientation)
        self.__graph_dict[s.id] = s

    def SetCurrentGraph(self, graph_id):
        if graph_id in range(len(self.__graph_dict.keys())):
            self.current_graph = self.__graph_dict[graph_id]
        else:
            raise TryingToLoadNonexistingGraph()

    def SaveCurrentGraph(self) -> int:
        if self.current_graph.id not in self.__saved_graph_dict.keys():
            self.__saved_graph_dict[self.current_graph.id] = []
            self.__saved_graph_dict[self.current_graph.id].append(copy.deepcopy(self.current_graph))
        else:
            self.__saved_graph_dict[self.current_graph.id].append(copy.deepcopy(self.current_graph))
        return len(self.__saved_graph_dict[self.current_graph.id]) - 1

    def LoadSavedGraph(self, graph_id: int = -1, saving_id: int = None) -> None:
        if graph_id in self.__saved_graph_dict.keys():
            if saving_id in range(len(self.__saved_graph_dict[graph_id])):
                self.current_graph = self.__saved_graph_dict[graph_id][saving_id]
            elif saving_id is None:
                self.current_graph = self.__saved_graph_dict[graph_id][len(self.__saved_graph_dict[graph_id]) - 1]
            else:
                raise TryingToLoadNonexistingSaving()
        else:
            raise TryingToLoadNonexistingSaving()

    def DeleteSaving(self, graph_id, saving_id):
        if graph_id in self.__saved_graph_dict.keys():
            if saving_id in range(len(self.__saved_graph_dict[graph_id])):
                self.__saved_graph_dict[graph_id].pop([saving_id])
            else:
                raise TryingToDeleteNonexistingSaving()
        else:
            raise TryingToDeleteNonexistingSaving()

    def DeleteSavedGraph(self, graph_id: int) -> None:
        if graph_id in self.__saved_graph_dict.keys():
            del self.__saved_graph_dict[graph_id]
        else:
            raise TryingToDeleteNonSavedGraph()

    def DeleteLoadedGraph(self, graph_id: int) -> None:
        if graph_id in self.__graph_dict.keys():
            del self.__graph_dict[graph_id]
        else:
            raise TryingToDeleteNonLoadedGraph()

    def DeleteCurrentGraph(self) -> None:
        if self.current_graph is not None:
            self.current_graph = None
        else:
            raise NoGraphLoadedToDelete()

    def GetLoadedGraph(self, id):
        return self.__graph_dict[id]

    def GetCurrentGraphInfo(self) -> str:
        if self.current_graph is not None:
            result = f'{self.current_graph.GetGraphInfoString()}'
        else:
            result = 'No graph is set as current'
        return result

    def GetLoadedGraphsInfo(self) -> str:
        result = ''
        if self.__graph_dict:
            for i in self.__graph_dict.values():
                result += i.GetGraphInfoString()
        result += 'No graphs are currently loaded'
        return result

    def GetLastLoadedGraphInfo(self) -> str:
        result = self.__graph_dict[len(self.__graph_dict) - 1].GetGraphInfoString()
        return result

    def GetLoadedGraphsAmount(self) -> int:
        return len(self.__graph_dict)

    def GetAmountOfSavingsOfCurrentGraph(self):
        return len(self.__saved_graph_dict[self.current_graph.id]) - 1

    def GetSavedGraphsAmount(self) -> int:
        return len(self.__saved_graph_dict)

    def GetSavingAmount(self, graph_id):
        return len(self.__saved_graph[graph_id])

    def FindTens(self, id1, id2):
        a = self.__graph_dict[id1]
        b = self.__graph_dict[id2]
        a1 = a.ConvertToNetworkxGraph()
        b1 = b.ConvertToNetworkxGraph()
        c1 = nx.tensor_product(a1, b1)
        return c1.edges

    def FindCart(self, id1, id2):
        a = self.__graph_dict[id1]
        b = self.__graph_dict[id2]
        a1 = a.ConvertToNetworkxGraph()
        b1 = b.ConvertToNetworkxGraph()
        c1 = nx.cartesian_product(a1, b1)
        return c1.edges
