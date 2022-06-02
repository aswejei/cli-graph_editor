from entities.eintities_space import GraphSpace
from entities.graph import Graph


class CLI:
    __gs = None

    @staticmethod
    def init():
        CLI.__gs = GraphSpace()
        print('Graph space was initialized')

    @staticmethod
    def main_menu():
        a = None
        while a != '14':
            print('Choose an option:\n'
                  '1 - Initialize graph and add it to graphspace\n'
                  '2 - Set one of graphs from the graphspace as the current graph\n'
                  '3 - Save snapshot of the currentgraph to a graphspace\'s graph state buffer\n'
                  '4 - Load one of the graph snapshots as current graph that had been taken during current session\n'
                  '5 - Delete one of the snapshots that have been saved to graph state buffer\n'
                  '6 - Delete all the snapshots of specified graph from the graph state buffer\n'
                  '7 - Delete one of the graphs added to the graphspace\n'
                  '8 - Delete the graph which is currently set as current graph\n'
                  '9 - Get info about the current graph\n'
                  '10 - Get info about all the graphs loaded to the graphspace\n'
                  '11 - Edit current graph\n'
                  '12 - Find tensor product of two graphs\n'
                  '13 - Find decarth product of two graphs\n'
                  '14 - Quit the CLI graph editor\n')
            k = {f'{i}' for i in range(1, 15)}
            a = input()
            while a not in k:
                print('Incorrect option number has been entered. Please try again\n')
                a = input()
            match int(a):
                case 1:
                    name = input('Enter name of a new graph\n')
                    b = {'oriented': True, 'nonoriented': False}
                    orient = input('Enter orientation of a new graph\n')
                    while orient not in b:
                        print('Incorrect option number has been entered. Please try again\n')
                        orient = input()
                    CLI.__gs.AddGraph(name=name, orientation=b[orient])
                    print('New graph had been successfully added to a graph space. See graph info below:')
                    print(CLI.__gs.GetLastLoadedGraphInfo())
                case 2:
                    name = input('Enter graph_id of the graph you would like to load\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetLoadedGraphsAmount())}
                    while name not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        name = input()
                    CLI.__gs.SetCurrentGraph(int(name))
                    print(f'Graph wit graph_id {name} had been successfully set as current. See graph info below:')
                    print(CLI.__gs.GetCurrentGraphInfo())
                case 3:
                    CLI.__gs.SaveCurrentGraph()
                    print(
                        f'Snapshot of current graph had been successfully saved with saving number {CLI.__gs.GetAmountOfSavingsOfCurrentGraph()}')
                case 4:
                    graph_id = input('Enter graph_id of graph saving of which you would like to load:\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetSavedGraphsAmount())}
                    while graph_id not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        graph_id = input()
                    saving = input('Enter saving number of graph which you would like to load:\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetSavingAmount())}
                    while saving not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        saving = input()
                    CLI.__gs.LoadSavedGraph(graph_id=int(graph_id), saving_id=int(saving))
                    print(f'Saving number {saving} of graph with id {graph_id} has been loaded successfully\n')
                case 5:
                    graph_id = input('Enter graph_id of graph saving of which you would like to delete:\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetSavedGraphsAmount())}
                    while graph_id not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        graph_id = input()
                    saving = input('Enter saving number of graph which you would like to delete:\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetSavingAmount())}
                    while saving not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        saving = input()
                    CLI.__gs.DeleteSaving(int(graph_id), int(saving))
                    print(f'Saving number {saving} of graph with id {graph_id} has been deleted successfully\n')
                case 6:
                    graph_id = input('Enter graph_id of graph all savings of which you would like to delete:\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetSavedGraphsAmount())}
                    while graph_id not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        graph_id = input()
                    CLI.__gs.DeleteSavedGraph(graph_id)
                    print(f'All savings of graph with id {graph_id} has been deleted successfully\n')
                case 7:
                    graph_id = input('Enter graph_id of graph which you would like to delete from the graphspace:\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetSavedGraphsAmount())}
                    while graph_id not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        graph_id = input()
                    CLI.__gs.DeleteLoadedGraph(graph_id)
                    print(f'Graph with id {graph_id} has been deleted from the graphspace successfully\n')
                case 8:
                    CLI.__gs.DeleteCurrentGraph()
                    print(f'Current graph has been dismissed successfully\n')
                case 9:
                    print(CLI.__gs.GetCurrentGraphInfo())
                case 10:
                    print(CLI.__gs.GetLoadedGraphsInfo())
                case 11:
                    CLI.graph_operations()
                case 12:
                    id1 = input('Enter graph_id of the first graph you would like multiplicate\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetLoadedGraphsAmount())}
                    while id1 not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        id1 = input()
                    id2 = input('Enter graph_id of the second graph you would like multiplicate\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetLoadedGraphsAmount())}
                    while id2 not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        id2 = input()
                    print(CLI.__gs.FindTens(int(id1), int(id2)))
                case 13:
                    id1 = input('Enter graph_id of the first graph you would like multiplicate\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetLoadedGraphsAmount())}
                    while id1 not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        id1 = input()
                    id2 = input('Enter graph_id of the second graph you would like multiplicate\n')
                    c = {f'{i}' for i in range(CLI.__gs.GetLoadedGraphsAmount())}
                    while id2 not in c:
                        print('Incorrect graph graph_id has been entered. Please try again\n')
                        id2 = input()
                    print(CLI.__gs.FindCart(int(id1), int(id2)))

    @staticmethod
    def graph_operations():
        if CLI.__gs.current_graph is None:
            print('You cant use graph operations if no graph is set as current')
        else:
            a = None
            while a != '13':
                print('Choose an option:\n'
                      '1 - Add node\n'
                      '2 - Add edge\n'
                      '3 - Delete node\n'
                      '4 - Delete edge\n'
                      '5 - Set node name\n'
                      '6 - Get graph info\n'
                      '7 - Set node color\n'
                      '8 - Check if graph is connected\n'
                      '9 - Make graph connected\n'
                      '10 - Find hamiltoninan paths\n'
                      '11 - Calculate center, radius and diamether for the graph\n'
                      '12 - Copy graph piece'
                      '13 - Go to main menu\n')
                k = {f'{i}' for i in range(1, 14)}
                a = input()
                while a not in k:
                    print('Incorrect option number has been entered. Please try again\n')
                    a = input()
                match int(a):
                    case 1:
                        print('Enter name of a new node:\n')
                        name = input()
                        print('Enter color of a new node\n')
                        color = input()
                        c = {i for i in Graph.colors_dict.keys()}
                        while color not in c:
                            print('Incorrect color has been entered. Please try again\n')
                            color = input()
                        print('Enter shape of a new node\n')
                        shape = input()
                        s = CLI.__gs.current_graph.AddNode(name=name, color=color, shape=shape)
                        print(s)
                    case 2:
                        print('Enter id of the first node in the edge\n')
                        node1_id = input()
                        c = {f'{i}' for i in CLI.__gs.current_graph.GetAllNodeIDs()}
                        while node1_id not in c:
                            print('Incorrect node id has been entered. Please try again\n')
                            node1_id = input()
                        print('Enter id of the second node in the edge\n')
                        node2_id = input()
                        c = {f'{i}' for i in CLI.__gs.current_graph.GetAllNodeIDs()}
                        while node2_id not in c:
                            print('Incorrect node id has been entered. Please try again\n')
                            node2_id = input()
                        print('Enter color of the new edge\n')
                        color = input()
                        s = CLI.__gs.current_graph.AddEdge(int(node1_id), int(node2_id), color=color)
                        print(s)
                    case 3:
                        print('Enter id of the node you would like to delete:\n')
                        del_id = input()
                        c = {f'{i}' for i in CLI.__gs.GetAllNodeIDs()}
                        while del_id not in c:
                            print('Incorrect node id has been entered. Please try again\n')
                            del_id = input()
                        CLI.__gs.current_graph.DeleteNode(int(del_id))
                        print(f'Node with id {del_id} has been deleted successfully with all the edges incedent to it')
                    case 4:
                        print('Enter id of the edge you would like to delete')
                        del_id = input()
                        c = {f'{i}' for i in CLI.__gs.GetAllEdgesIDs()}
                        while del_id not in c:
                            print('Incorrect edge id has been entered. Please try again\n')
                            del_id = input()
                        CLI.__gs.current_graph.DeleteEdge(int(del_id))
                        print(f'Edge with id {del_id} has been deleted successfully')
                    case 5:
                        print('Enter id of the node you would like to rename:\n')
                        node_id = input()
                        c = {f'{i}' for i in CLI.__gs.GetAllNodeIDs()}
                        while node_id not in c:
                            print('Incorrect node id has been entered. Please try again\n')
                            node_id = input()
                        name = input('Enter new name for the node: ')
                        CLI.__gs.current_graph.SetNodeName(int(node_id), name)
                        print(f'New name for the node with id {node_id} has been set successfully')
                    case 6:
                        print(CLI.__gs.current_graph.GetGraphInfoString())
                    case 7:
                        print('Enter id of the node you would like to recolor:\n')
                        node_id = input()
                        c = {f'{i}' for i in CLI.__gs.GetAllNodeIDs()}
                        while node_id not in c:
                            print('Incorrect node id has been entered. Please try again\n')
                            node_id = input()
                        name = input('Enter new color for the node: ')
                        CLI.__gs.current_graph.SetNodeName(int(node_id), name)
                        print(f'New color for the node with id {node_id} has been set successfully')
                    case 8:
                        a = CLI.__gs.current_graph.IsConnected()
                        if a == 0:
                            print('Graph is not connected')
                        else:
                            print('Graph is connected')
                    case 9:
                        CLI.__gs.current_graph.MakeConnected()
                        print('Graph has been made connected. Current graph state:')
                        print(CLI.__gs.current_graph.GetGraphInfoString())
                    case 10:
                        print('Hamilthonian path is:')
                        print(CLI.__gs.current_graph.GetHamiltonianPath())
                    case 11:
                        a = CLI.__gs.current_graph.GetDiamRadCent()
                        print(f'Diamether is {a[0]}, radius is {a[1]}, center is {a[2]}')
                    case 12:
