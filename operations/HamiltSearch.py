from entities.graph import Graph


class HamiltSearch:
    __dfs_visited_nodes=[]
    __dfs_start_node=None
    __dfs_current_node=None

    @staticmethod
    def CheckIfHamilt(graph: Graph) -> bool:
        HamiltSearch.__dfs_start_node=graph.nodes_dict[0]

    

