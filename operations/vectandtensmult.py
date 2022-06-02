import networkx as nx

from entities.graph import Graph


def DecMultiplication(a: Graph, b: Graph):
    a1=a.ConvertToNetworkxGraph()
    b1=b.ConvertToNetworkxGraph()
    a1
    c=nx.cartesian_product(a1, b1)
    return c.edges


def TensorMultiplication(a: Graph, b: Graph):
    a1 = a.ConvertToNetworkxGraph()
    b1 = b.ConvertToNetworkxGraph()
    c = nx.tensor_product(a1, b1)
    return c.edges